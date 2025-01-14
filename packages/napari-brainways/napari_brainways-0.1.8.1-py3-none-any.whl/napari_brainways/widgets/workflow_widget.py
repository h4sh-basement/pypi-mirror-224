from __future__ import annotations

import functools
import os
from dataclasses import replace
from pathlib import Path
from typing import Callable, List, Union

import importlib_resources
import PIL.Image
from bg_atlasapi.list_atlases import get_all_atlases_lastversions
from brainways.pipeline.brainways_params import BrainwaysParams
from brainways.project.brainways_project import BrainwaysProject
from brainways.project.info_classes import ProjectSettings
from brainways.utils.cell_detection_importer.utils import (
    cell_detection_importer_types,
    get_cell_detection_importer,
)
from magicgui import magicgui
from magicgui.widgets import Image, request_values
from qtpy.QtCore import Qt
from qtpy.QtWidgets import (
    QDialog,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from napari_brainways.controllers.base import Controller
from napari_brainways.widgets.create_subject_dialog import CreateSubjectDialog


class WorkflowView(QWidget):
    def __init__(self, controller, steps: List[Controller]):
        super().__init__(controller)
        self.controller = controller
        self.steps = steps
        self._prev_path = str(Path.home())

        self.project_buttons = ProjectButtons(
            open_project=self.on_open_project_clicked,
            edit_project=self.on_edit_project_clicked,
            new_project=self.on_create_project_clicked,
        )
        self.project_actions_section = ProjectActionsSection(
            import_cells=self.on_import_cells_clicked,
            run_cell_detector=self.on_run_cell_detector_clicked,
        )
        self.subject_navigation = SubjectControls(
            select_callback=self.select_subject,
            prev_callback=self.controller.prev_subject,
            next_callback=self.controller.next_subject,
            add_subject_callback=self.on_add_subject_clicked,
            edit_subject_callback=self.on_edit_subject_clicked,
            visible=False,
        )
        self.image_navigation = NavigationControls(
            title="<b>Select Image:</b> [b/n]",
            label="Image",
            select_callback=self.select_image,
            prev_callback=self.controller.prev_image,
            next_callback=self.controller.next_image,
        )
        self.step_buttons = StepButtons(
            steps=steps, clicked=self.on_step_clicked, title="<b>Steps:</b> [PgUp/PgDn]"
        )
        self.step_controls = StepControls(steps=steps)
        self.progress_bar = ProgressBar()
        self.header_section = HeaderSection(progress_bar=self.progress_bar)
        self.subject_controls = self._stack_widgets(
            [
                self.image_navigation,
                self.step_buttons,
                self.step_controls,
                self.project_actions_section,
            ]
        )

        self.all_widgets = self._stack_widgets(
            [
                self.header_section,
                self.project_buttons,
                self.subject_navigation,
                self.subject_controls,
            ]
        )
        self.all_widgets.layout().addStretch()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.all_widgets)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.scroll_area)

        self.subject_controls.hide()

        # self.setMinimumWidth(400)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def _stack_widgets(self, widgets) -> QWidget:
        widget = QWidget(self)
        widget.setLayout(QVBoxLayout())
        widget.layout().setContentsMargins(0, 0, 0, 0)
        for section in widgets:
            widget.layout().addWidget(section)
        return widget

    def on_create_project_clicked(self, _=None):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "New Brainways Project",
            self._prev_path,
            "Brainways Project File (*.bwp)",
        )
        if path == "":
            return

        if Path(path).suffix == "":
            path += ".bwp"

        self._prev_path = str(Path(path).parent)

        available_atlases = list(get_all_atlases_lastversions().keys())
        user_values = request_values(
            title="New Brainways Project",
            atlas=dict(
                value="whs_sd_rat_39um",
                widget_type="ComboBox",
                options=dict(choices=available_atlases),
                annotation=str,
                label="Atlas",
            ),
            condition_names=dict(
                value="condition1;condition2",
                annotation=str,
                label="Conditions",
            ),
        )
        if user_values is None:
            return

        settings = ProjectSettings(
            atlas=user_values["atlas"],
            channel=0,
            condition_names=user_values["condition_names"].split(";"),
        )
        project = BrainwaysProject.create(path=path, settings=settings, lazy_init=True)
        self.controller.open_project_async(project.path)

    def on_edit_project_clicked(self, _=None):
        settings: ProjectSettings = self.controller.project.settings
        user_values = request_values(
            title="Edit Brainways Project",
            condition_names=dict(
                value=";".join(settings.condition_names),
                annotation=str,
                label="Conditions",
            ),
        )
        if user_values is None:
            return

        self.controller.project.settings = replace(
            settings, condition_names=user_values["condition_names"].split(";")
        )
        self.controller.project.save()

    def on_add_subject_clicked(self, _=None):
        values = request_values(
            subject_id=dict(annotation=str, label="Subject ID:"),
            title="New Subject",
        )
        if values is None or values["subject_id"] == "":
            return

        subject_id = values["subject_id"]
        dialog = CreateSubjectDialog(project=self.controller.project, parent=self)
        dialog.new_subject(subject_id=subject_id, conditions={})
        result = dialog.exec()
        if result == QDialog.DialogCode.Rejected:
            return
        subject_index = self.controller.project.subjects.index(dialog.subject)
        self.on_project_changed(n_subjects=len(self.controller.project))
        self.controller.set_subject_index_async(subject_index)

    def on_edit_subject_clicked(self, _=None):
        dialog = CreateSubjectDialog(project=self.controller.project, parent=self)
        dialog.edit_subject_async(
            subject_index=self.controller.current_subject_index,
            document_index=self.controller.current_valid_document_index,
        )
        result = dialog.exec()
        if result == QDialog.DialogCode.Rejected:
            return
        self.on_subject_changed()
        self.controller.set_document_index_async(
            image_index=0, force=True, persist_current_params=False
        )

    def on_open_project_clicked(self, _=None):
        kwargs = {}
        if "SNAP" in os.environ:
            kwargs["options"] = QFileDialog.DontUseNativeDialog

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Project",
            self._prev_path,
            "Brainways Project (*.bwp)",
            **kwargs,
        )
        if path == "":
            return
        self._prev_path = str(Path(path).parent)
        self.controller.open_project_async(Path(path))

    def on_project_changed(self, n_subjects: int):
        self.project_buttons.project_opened()
        self.subject_navigation.project_opened(n_subjects)
        self.set_step(0)

    def on_subject_changed(self):
        self.image_navigation.max = self.controller.subject_size
        self.subject_controls.show()

    def select_subject(self, value: int):
        self.controller.set_subject_index_async(value - 1)

    def select_image(self, value: int):
        self.controller.set_document_index_async(value - 1)

    def set_step(self, step_index: int):
        self.step_buttons.set_step(step_index)
        self.step_controls.set_step(step_index)

    def on_step_clicked(self, _=None, step_index: int = 0):
        self.set_step(step_index)
        self.controller.set_step_index_async(step_index)

    def on_prev_step_clicked(self, _=None):
        self.controller.prev_step()

    def on_next_step_clicked(self, _=None):
        self.controller.next_step()

    def on_run_workflow_clicked(self, _=None):
        self.controller.run_workflow_async()

    def on_save_button_clicked(self, _=None):
        self.controller.save_subject()

    def on_import_cells_clicked(self, _=None):
        kwargs = {}
        if "SNAP" in os.environ:
            kwargs["options"] = QFileDialog.DontUseNativeDialog

        path = QFileDialog.getExistingDirectory(
            self,
            "Import Cells",
            self._prev_path,
            **kwargs,
        )
        if path == "":
            return
        self._prev_path = str(Path(path))

        values = request_values(
            title="Import Cell Detections",
            importer_type=dict(
                value="keren",
                widget_type="ComboBox",
                options=dict(choices=cell_detection_importer_types()),
                annotation=str,
                label="Importer Type",
            ),
        )
        if values is None:
            return

        Importer = get_cell_detection_importer(values["importer_type"])
        importer_params = {}
        if Importer.parameters:
            importer_params = request_values(
                title="Import Cell Detections Parameters", values=Importer.parameters
            )
            if importer_params is None:
                return

        self.controller.import_cell_detections_async(
            path=Path(path), importer=Importer(**importer_params)
        )

    def on_run_cell_detector_clicked(self, _=None):
        self.controller.run_cell_detector_async()

    def set_subject_index(self, subject_index: int):
        self.subject_navigation.value = subject_index

    def set_image_index(self, image_index: int):
        self.image_navigation.value = image_index

    def update_progress_bar(self, value: int = None, text: str = None):
        if text is not None:
            self.progress_bar.text = text
        if value is not None:
            self.progress_bar.value = value
        elif value is None and self.progress_bar.max > 0:
            self.progress_bar.value += 1

    def show_progress_bar(self, max_value: int = 0, label: str = ""):
        self.all_widgets.setEnabled(False)
        self.progress_bar.value = 0
        self.progress_bar.text = label
        self.progress_bar.max = max_value
        self.header_section.show_progress()
        self.scroll_area.verticalScrollBar().setValue(0)

    def hide_progress_bar(self):
        self.all_widgets.setEnabled(True)
        self.header_section.hide_progress()

    def update_enabled_steps(self):
        self.step_buttons.update_enabled(self.controller.current_params)


class TitledGroupBox(QWidget):
    def __init__(
        self,
        title: Union[str, QLabel],
        widgets: List[QWidget | None],
        layout: str = "vertical",
        visible: bool = True,
    ):
        super().__init__()
        groupbox = QGroupBox()
        if layout == "vertical":
            groupbox.setLayout(QVBoxLayout())
        else:
            groupbox.setLayout(QHBoxLayout())

        for widget in widgets:
            if widget is not None:
                groupbox.layout().addWidget(widget)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel(title) if isinstance(title, str) else title)
        self.layout().addWidget(groupbox)

        self.visible = visible

    @property
    def visible(self) -> bool:
        return self.isVisible()

    @visible.setter
    def visible(self, value: bool):
        self.setVisible(value)


class ProjectButtons(TitledGroupBox):
    def __init__(
        self,
        open_project: Callable,
        edit_project: Callable,
        new_project: Callable,
    ):
        self.open_project = QPushButton("Open")
        self.edit_project = QPushButton("Edit")
        self.new_project = QPushButton("New")

        self.open_project.clicked.connect(open_project)
        self.edit_project.clicked.connect(edit_project)
        self.new_project.clicked.connect(new_project)

        super().__init__(
            title="<b>Project:</b>",
            widgets=[self.open_project, self.edit_project, self.new_project],
            layout="horizontal",
        )

        self.project_closed()

    def project_opened(self):
        self.edit_project.setVisible(True)

    def project_closed(self):
        self.edit_project.setVisible(False)


class ProjectActionsSection(TitledGroupBox):
    def __init__(
        self,
        import_cells: Callable,
        run_cell_detector: Callable,
    ):
        self.import_cells = QPushButton("Import Cell Detections")
        self.run_cell_detector = QPushButton("Run Cell Detector")

        self.import_cells.clicked.connect(import_cells)
        self.run_cell_detector.clicked.connect(run_cell_detector)

        super().__init__(
            title="<b>Project Actions:</b>",
            widgets=[self.run_cell_detector, self.import_cells],
        )


class NavigationControls(TitledGroupBox):
    def __init__(
        self,
        title: str,
        label: str,
        select_callback: Callable,
        prev_callback: Callable,
        next_callback: Callable,
        visible: bool = True,
    ):
        self.selector_widget = magicgui(
            select_callback,
            auto_call=True,
            value={
                "widget_type": "Slider",
                "label": f"{label} #",
                "min": 1,
                "max": 1,
            },
        )
        self.selector_max_label = QLabel("")
        self.prev_button = QPushButton("< Previous")
        self.next_button = QPushButton("Next >")

        self.prev_button.clicked.connect(prev_callback)
        self.next_button.clicked.connect(next_callback)

        super().__init__(title=title, widgets=self._build_layout(), visible=visible)

    def _build_layout(self) -> List[QWidget]:
        self.selector_widget.native.layout().setContentsMargins(0, 0, 0, 0)

        selector = QWidget()
        selector.setLayout(QHBoxLayout())
        selector.layout().addWidget(self.selector_widget.native)
        selector.layout().addWidget(self.selector_max_label)

        buttons = QWidget()
        buttons.setLayout(QHBoxLayout())
        buttons.layout().addWidget(self.prev_button)
        buttons.layout().addWidget(self.next_button)

        return [selector, buttons]

    @property
    def max(self):
        return self.selector_widget.value.max

    @max.setter
    def max(self, value: int):
        self.selector_widget.value.max = value
        self.selector_max_label.setText(f"/ {value}")

    @property
    def visible(self) -> bool:
        return self.isVisible()

    @visible.setter
    def visible(self, value: bool):
        self.setVisible(value)

    @property
    def value(self):
        return self.selector_widget.value

    @value.setter
    def value(self, value):
        self.selector_widget._auto_call = False
        self.selector_widget.value.value = value
        self.selector_widget._auto_call = True


class SubjectControls(NavigationControls):
    def __init__(
        self,
        select_callback: Callable,
        prev_callback: Callable,
        next_callback: Callable,
        add_subject_callback: Callable,
        edit_subject_callback: Callable,
        visible: bool = True,
    ):
        self.add_subject_button = QPushButton("Add Subject")
        self.add_subject_button.clicked.connect(add_subject_callback)

        self.edit_subject_button = QPushButton("Edit Subject")
        self.edit_subject_button.clicked.connect(edit_subject_callback)

        super().__init__(
            title="<b>Select Subject:</b> [B/N]",
            label="Subject",
            select_callback=select_callback,
            prev_callback=prev_callback,
            next_callback=next_callback,
            visible=visible,
        )

    def _build_layout(self) -> List[QWidget]:
        widgets = super()._build_layout()
        widgets.append(self.add_subject_button)
        widgets.append(self.edit_subject_button)
        return widgets

    def project_opened(self, n_subjects: int):
        self.visible = True
        if n_subjects == 0:
            navigation_visible = False
        else:
            self.max = n_subjects
            navigation_visible = True

        self.selector_widget.visible = navigation_visible
        self.next_button.setVisible(navigation_visible)
        self.prev_button.setVisible(navigation_visible)
        self.edit_subject_button.setVisible(navigation_visible)

    def project_closed(self, n_subjects: int):
        self.visible = False


class StepButtons(TitledGroupBox):
    def __init__(self, steps: List[Controller], clicked: Callable, title: str):
        self.steps = steps
        self.buttons = []
        for i, step in enumerate(steps):
            button = QPushButton(step.name)
            button.clicked.connect(functools.partial(clicked, step_index=i))
            button.clicked.connect(functools.partial(self.set_step, step_index=i))
            button.setCheckable(True)
            self.buttons.append(button)

        super().__init__(title=title, widgets=self.buttons)

    def set_step(self, step_index: int):
        for i, button in enumerate(self.buttons):
            button.setChecked(i == step_index)

    def update_enabled(self, params: BrainwaysParams):
        for step, button in zip(self.steps, self.buttons):
            button.setEnabled(step.enabled(params))


class StepControls(TitledGroupBox):
    def __init__(self, steps: List[Controller]):
        self.steps = steps
        self.title = QLabel("")
        self.widgets = [step.widget for step in steps]
        super().__init__(title=self.title, widgets=self.widgets)

    def set_step(self, step_index: int):
        for i, widget in enumerate(self.widgets):
            if widget is not None:
                widget.setVisible(i == step_index)

        self.setVisible(self.steps[step_index].widget is not None)
        self.title.setText(f"<b>{self.steps[step_index].name} Parameters:</b>")


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self._label_widget = QLabel(self)
        self._progress_bar = QProgressBar()
        self._progress_bar.setValue(0)
        self._progress_bar.setMaximum(0)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self._label_widget)
        self.layout().addWidget(self._progress_bar)

        self.hide()

    @property
    def max(self) -> int:
        return self._progress_bar.maximum()

    @max.setter
    def max(self, value: int):
        self._progress_bar.setMaximum(value)

    @property
    def value(self) -> int:
        return self._progress_bar.value()

    @value.setter
    def value(self, value: int):
        self._progress_bar.setValue(value)

    @property
    def text(self) -> str:
        return self._label_widget.text()

    @text.setter
    def text(self, value: str):
        self._label_widget.setText(value)


class HeaderSection(QWidget):
    def __init__(self, progress_bar: ProgressBar):
        super().__init__()

        self.header = self._build_header()
        self.progress_bar = progress_bar
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.header)
        self.layout().addWidget(progress_bar)
        self.setMinimumHeight(80)

    def _build_header(self):
        package = Path(importlib_resources.files("napari_brainways"))
        logo = Image(value=PIL.Image.open(package / "resources/logo.png"))
        title = QLabel("Brainways")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        header_container = QWidget()
        header_container.setLayout(QHBoxLayout())
        header_container.layout().addWidget(logo.native)
        header_container.layout().addWidget(title)

        # header_container.layout().setAlignment(title, Qt.AlignLeft)
        return header_container

    def show_progress(self):
        self.header.hide()
        self.progress_bar.show()

    def hide_progress(self):
        self.header.show()
        self.progress_bar.hide()
