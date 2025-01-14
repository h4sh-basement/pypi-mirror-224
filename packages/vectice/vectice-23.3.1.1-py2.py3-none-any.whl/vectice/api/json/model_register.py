from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from vectice.api.json.metric import MetricInput

if TYPE_CHECKING:
    from vectice.api.json.model_version import ModelVersionOutput, ModelVersionStatus
    from vectice.models.property import Property


class ModelType(Enum):
    """Enumeration of the different model types."""

    ANOMALY_DETECTION = "ANOMALY_DETECTION"
    CLASSIFICATION = "CLASSIFICATION"
    CLUSTERING = "CLUSTERING"
    OTHER = "OTHER"
    RECOMMENDATION_MODELS = "RECOMMENDATION_MODELS"
    REGRESSION = "REGRESSION"
    TIME_SERIES = "TIME_SERIES"


class ModelRegisterOutput(dict):
    @property
    def model_version(self) -> ModelVersionOutput:
        from vectice.api.json.model_version import ModelVersionOutput

        return ModelVersionOutput(**self["modelVersion"])

    @property
    def use_existing_model(self) -> bool:
        return bool(self["useExistingModel"])

    # TODO: complete the jobrun property
    @property
    def job_run(self) -> str:
        return str(self["jobRun"])


class ModelRegisterInput(dict):
    @property
    def name(self) -> str:
        return str(self["name"])

    @property
    def model_type(self) -> ModelType:
        return ModelType(**self["modelType"])

    @property
    def properties(self) -> Property:
        from vectice.models.property import Property

        return Property(**self["properties"])

    @property
    def metrics(self) -> list[MetricInput]:
        return [MetricInput(**metric) for metric in self["metrics"]]

    @property
    def status(self) -> ModelVersionStatus:
        from vectice.api.json.model_version import ModelVersionStatus

        return ModelVersionStatus(self["status"])

    @property
    def framework(self) -> str | None:
        return str(self["framework"])

    @property
    def type(self) -> str:
        return str(self["type"])

    @property
    def algorithm_name(self) -> str | None:
        return str(self["algorithmName"])

    @property
    def uri(self) -> str:
        return str(self["uri"])

    @property
    def derived_from(self) -> list[int]:
        return [(self["inputs"])]

    @property
    def context(self) -> ModelVersionContextInput:
        return ModelVersionContextInput(self["context"])


class ModelVersionContextInput(dict):
    @property
    def url(self) -> str:
        return str(self["url"])

    @property
    def run(self) -> str:
        return str(self["run"])
