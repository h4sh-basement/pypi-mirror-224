# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
The ``mlflow.models`` module provides an API for saving machine learning models in
"flavors" that can be understood by different downstream tools.

The built-in flavors are:

- :py:mod:`mlflow.pyfunc`
- :py:mod:`mlflow.h2o`
- :py:mod:`mlflow.keras`
- :py:mod:`mlflow.lightgbm`
- :py:mod:`mlflow.pytorch`
- :py:mod:`mlflow.sklearn`
- :py:mod:`mlflow.spark`
- :py:mod:`mlflow.statsmodels`
- :py:mod:`mlflow.tensorflow`
- :py:mod:`mlflow.xgboost`
- :py:mod:`mlflow.spacy`
- :py:mod:`mlflow.fastai`
- :py:mod:`mlflow.paddle`

For details, see `MLflow Models <../models.html>`_.
"""

from mlflow.models.model import Model
from mlflow.models.flavor_backend import FlavorBackend
from mlflow.utils.environment import infer_pip_requirements
from azureml.evaluate.mlflow.models.evaluation import evaluate, EvaluationArtifact, EvaluationResult, list_evaluators
# from mlflow.models import EvaluationArtifact, EvaluationResult, list_evaluators

__all__ = [
    "Model",
    "FlavorBackend",
    "infer_pip_requirements",
    "evaluate",
    "EvaluationArtifact",
    "EvaluationResult",
    "list_evaluators",
]


# Under skinny-mlflow requirements, the following packages cannot be imported
# because of lack of numpy/pandas library, so wrap them with try...except block
try:
    from mlflow.models.signature import ModelSignature, infer_signature  # pylint: disable=unused-import
    from mlflow.models.utils import ModelInputExample  # pylint: disable=unused-import

    __all__ += [
        "ModelSignature",
        "ModelInputExample",
        "infer_signature",
    ]
except ImportError:
    pass
