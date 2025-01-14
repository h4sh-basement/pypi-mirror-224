from edc_adverse_event.pdf_reports import AeReport
from edc_adverse_event.view_mixins import AeListboardViewMixin
from reportlab.lib.units import cm


class CustomAeReport(AeReport):
    logo_data = {
        "app_label": "intecomm_edc",
        "filename": "meta_logo.png",
        "first_page": (4.0 * cm, 0.83 * cm),
        "later_pages": (3.0 * cm, 0.625 * cm),
    }


class AeListboardView(AeListboardViewMixin):
    pdf_report_cls = CustomAeReport
