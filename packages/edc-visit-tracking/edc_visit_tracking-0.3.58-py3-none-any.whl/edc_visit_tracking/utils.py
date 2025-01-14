from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Type, TypeVar

from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .exceptions import RelatedVisitModelError

if TYPE_CHECKING:
    from edc_list_data.model_mixins import ListModelMixin

    from .models import SubjectVisitMissed
    from .typing_stubs import RelatedVisitProtocol

    ListModel = TypeVar("ListModel", bound=ListModelMixin)


def get_related_visit_model() -> str:
    """Returns the label_lower of the related visit model for this
    project.

    One `related visit model` allowed per project.
    """
    return getattr(settings, "SUBJECT_VISIT_MODEL", "edc_visit_tracking.subjectvisit")


def get_related_visit_model_cls() -> Type[RelatedVisitProtocol]:
    model_cls = django_apps.get_model(get_related_visit_model())
    if model_cls._meta.proxy:
        # raise for now until we have a solution
        raise RelatedVisitModelError(
            f"Not allowed. Related visit model may not be a proxy model. Got {model_cls}. "
        )
    return model_cls


def get_subject_visit_model() -> str:
    warnings.warn(
        "This func has been renamed to `get_related_visit_model`.",
        DeprecationWarning,
        stacklevel=2,
    )
    return get_related_visit_model()


def get_subject_visit_model_cls() -> Type[RelatedVisitProtocol]:
    warnings.warn(
        "This func has been renamed to `get_related_visit_model_cls`.",
        DeprecationWarning,
        stacklevel=2,
    )
    return get_related_visit_model_cls()


def get_subject_visit_missed_model() -> str:
    error_msg = (
        "Settings attribute `SUBJECT_VISIT_MISSED_MODEL` not set. Update settings. "
        "For example, `SUBJECT_VISIT_MISSED_MODEL=meta_subject.subjectvisitmissed`. "
        "See also `SubjectVisitMissedModelMixin`."
    )
    try:
        model = settings.SUBJECT_VISIT_MISSED_MODEL
    except AttributeError as e:
        raise ImproperlyConfigured(f"{error_msg} Got {e}.")
    else:
        if not model:
            raise ImproperlyConfigured(f"{error_msg} Got None.")
    return model


def get_subject_visit_missed_model_cls() -> Type[SubjectVisitMissed]:
    return django_apps.get_model(get_subject_visit_missed_model())
