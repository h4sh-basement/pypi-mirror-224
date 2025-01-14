from __future__ import annotations

from typing import TYPE_CHECKING

import napari
import napari.layers
import numpy as np
from brainways.pipeline.brainways_params import BrainwaysParams
from brainways.pipeline.brainways_pipeline import PipelineStep

from napari_brainways.controllers.base import Controller
from napari_brainways.utils import update_layer_contrast_limits

if TYPE_CHECKING:
    from napari_brainways.brainways_ui import BrainwaysUI


class AnnotationViewerController(Controller):
    def __init__(self, ui: BrainwaysUI):
        super().__init__(ui)
        self.input_layer: napari.layers.Image | None = None
        self.annotations_layer: napari.layers.Image | None = None
        self._image: np.ndarray | None = None
        self._params: BrainwaysParams | None = None

    @property
    def name(self) -> str:
        return "Annotation Viewer"

    def default_params(self, image: np.ndarray, params: BrainwaysParams):
        return params

    def run_model(self, image: np.ndarray, params: BrainwaysParams) -> BrainwaysParams:
        return params

    @staticmethod
    def has_current_step_params(params: BrainwaysParams) -> bool:
        return True

    @staticmethod
    def enabled(params: BrainwaysParams) -> bool:
        return params.tps is not None

    def open(self) -> None:
        if self._is_open:
            return

        self.input_layer = self.ui.viewer.add_image(np.zeros((10, 10)), name="Image")
        self.annotations_layer = self.ui.viewer.add_labels(
            np.zeros((10, 10), np.int32), name="Annotations"
        )
        self.annotations_layer.mouse_move_callbacks.append(self.on_mouse_move)
        self._is_open = True

    def on_mouse_move(self, _layer, event):
        struct_id = self.annotations_layer.get_value(event.position, world=True)
        if struct_id and struct_id in self.pipeline.atlas.brainglobe_atlas.structures:
            struct_name = self.pipeline.atlas.brainglobe_atlas.structures[struct_id][
                "name"
            ]
        else:
            struct_name = ""
        _layer.help = struct_name

    def close(self) -> None:
        self.ui.viewer.layers.remove(self.input_layer)
        self.ui.viewer.layers.remove(self.annotations_layer)
        self.input_layer = None
        self.annotations_layer = None
        self._image = None
        self._params = None
        self._is_open = False

    def show(
        self,
        params: BrainwaysParams,
        image: np.ndarray | None = None,
        from_ui: bool = False,
    ) -> None:
        self._params = params
        if image is not None:
            self._image = image
            registered_image = self.pipeline.transform_image(
                image=self._image, params=params, until_step=PipelineStep.TPS
            )
            self.input_layer.data = registered_image
            update_layer_contrast_limits(self.input_layer)
            self.annotations_layer.data = self.pipeline.get_atlas_slice(
                params
            ).annotation.numpy()
            self.ui.viewer.reset_view()

    @property
    def params(self) -> BrainwaysParams:
        return self._params
