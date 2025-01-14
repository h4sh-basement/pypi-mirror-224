from django.conf import settings
from django.db import models
from edc_model.validators import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start
from edc_utils import get_utcnow
from edc_visit_schedule.model_mixins import CrfScheduleModelMixin

from ..base import VisitMethodsModelMixin


class VisitTrackingRequisitionModelMixin(
    VisitMethodsModelMixin,
    CrfScheduleModelMixin,
    models.Model,
):
    """Model mixin used by RequisitionModelMixin (edc-lab)"""

    subject_visit = models.ForeignKey(settings.SUBJECT_VISIT_MODEL, on_delete=models.PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[datetime_not_before_study_start, datetime_not_future],
        default=get_utcnow,
        help_text=(
            "If reporting today, use today's date/time, otherwise use "
            "the date/time this information was reported."
        ),
    )

    @classmethod
    def related_visit_model_attr(cls) -> str:
        # assuming subject_visit
        return "subject_visit"

    class Meta:
        abstract = True
