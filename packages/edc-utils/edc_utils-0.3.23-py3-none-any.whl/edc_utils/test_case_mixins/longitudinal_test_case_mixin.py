from django.apps import apps as django_apps
from django.test import TestCase
from edc_action_item import site_action_items
from edc_appointment.models import Appointment
from edc_consent import site_consents
from edc_facility.import_holidays import import_holidays
from edc_reference import site_reference_configs
from edc_registration.models import RegisteredSubject
from edc_reportable import site_reportables
from edc_reportable.grading_data.daids_july_2017 import grading_data
from edc_reportable.normal_data.africa import normal_data
from edc_visit_schedule import site_visit_schedules
from edc_visit_tracking.constants import SCHEDULED
from visit_schedule_app.consents import v1_consent
from visit_schedule_app.models import SubjectConsent
from visit_schedule_app.visit_schedule import visit_schedule

from edc_utils import get_utcnow


class LongitudinalTestCaseMixin(TestCase):
    visit_schedule = visit_schedule

    @classmethod
    def setUpClass(cls):
        site_reportables._registry = {}
        site_action_items.registry = {}
        site_reference_configs.registry = {}
        site_visit_schedules._registry = {}
        site_visit_schedules.loaded = False
        super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        site_reportables.register(
            name="my_reportables", normal_data=normal_data, grading_data=grading_data
        )
        site_visit_schedules.register(cls.visit_schedule)
        site_reference_configs.register_from_visit_schedule(
            visit_models={"edc_appointment.appointment": "edc_visit_tracking.subjectvisit"}
        )
        site_consents.register(v1_consent)
        import_holidays()

    @staticmethod
    def enroll(subject_identifier=None):
        subject_identifier = subject_identifier or "1111111"
        subject_consent = SubjectConsent.objects.create(
            subject_identifier=subject_identifier, consent_datetime=get_utcnow()
        )
        _, schedule = site_visit_schedules.get_by_onschedule_model(
            "visit_schedule_app.onschedule"
        )
        schedule.put_on_schedule(
            subject_identifier=subject_consent.subject_identifier,
            onschedule_datetime=subject_consent.consent_datetime,
        )
        return subject_identifier

    @staticmethod
    def fake_enroll():
        subject_identifier = "2222222"
        RegisteredSubject.objects.create(subject_identifier=subject_identifier)
        return subject_identifier

    def create_visits(self, subject_identifier):
        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier,
            visit_code="1000",
            visit_code_sequence=0,
        )
        self.subject_visit_baseline = django_apps.get_model(
            "edc_visit_tracking.subjectvisit"
        ).objects.create(
            report_datetime=get_utcnow(),
            appointment=appointment,
            reason=SCHEDULED,
            visit_code="1000",
            visit_code_sequence=0,
        )

        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier,
            visit_code="2000",
            visit_code_sequence=0,
        )
        self.subject_visit_followup = django_apps.get_model(
            "edc_visit_tracking.subjectvisit"
        ).objects.create(
            report_datetime=get_utcnow(),
            appointment=appointment,
            reason=SCHEDULED,
            visit_code="4000",
            visit_code_sequence=0,
        )
