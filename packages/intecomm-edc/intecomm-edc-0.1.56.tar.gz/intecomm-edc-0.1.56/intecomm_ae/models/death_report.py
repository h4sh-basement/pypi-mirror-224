from django.db import models
from edc_adverse_event.model_mixins import DeathReportModelMixin
from edc_model.models import BaseUuidModel

from ..model_mixins import DeathReportModelMixin as MyDeathReportModelMixin


class DeathReport(MyDeathReportModelMixin, DeathReportModelMixin, BaseUuidModel):
    study_day = models.IntegerField(default=0, editable=False, help_text="not used")

    class Meta(DeathReportModelMixin.Meta, BaseUuidModel.Meta):
        pass
