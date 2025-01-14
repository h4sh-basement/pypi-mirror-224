from django.contrib import admin
from edc_action_item import ActionItemModelAdminMixin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_model_admin.history import SimpleHistoryAdmin
from edc_protocol_incident.modeladmin_mixins import ProtocolIncidentModelAdminMixin
from edc_sites.admin import SiteModelAdminMixin

from ..admin_site import intecomm_prn_admin
from ..forms import ProtocolIncidentForm
from ..models import ProtocolIncident


@admin.register(ProtocolIncident, site=intecomm_prn_admin)
class ProtocolIncidentAdmin(
    SiteModelAdminMixin,
    ProtocolIncidentModelAdminMixin,
    ActionItemModelAdminMixin,
    ModelAdminSubjectDashboardMixin,
    SimpleHistoryAdmin,
):
    form = ProtocolIncidentForm
