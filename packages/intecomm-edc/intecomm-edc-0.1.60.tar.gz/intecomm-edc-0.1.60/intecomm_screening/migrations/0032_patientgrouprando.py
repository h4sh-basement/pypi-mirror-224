# Generated by Django 4.1.7 on 2023-05-11 23:08

from django.db import migrations
import edc_sites.model_mixins
import intecomm_group.models.patient_group


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_group", "0012_alter_historicalpatientgroup_status_and_more"),
        ("intecomm_screening", "0031_alter_historicalpatientlog_next_appt_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientGroupRando",
            fields=[],
            options={
                "verbose_name": "Patient group randomization",
                "verbose_name_plural": "Patient group randomization",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("intecomm_group.patientgroup",),
            managers=[
                ("on_site", edc_sites.model_mixins.CurrentSiteManager()),
                ("objects", intecomm_group.models.patient_group.PatientGroupManager()),
            ],
        ),
    ]
