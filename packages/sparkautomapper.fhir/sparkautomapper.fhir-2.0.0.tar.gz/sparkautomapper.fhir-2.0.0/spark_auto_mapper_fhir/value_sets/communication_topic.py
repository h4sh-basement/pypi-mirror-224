from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CommunicationTopicCode(GenericTypeCode):
    """
    CommunicationTopic
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
        Codes describing the purpose or content of the communication.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/communication-topic
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/communication-topic"


class CommunicationTopicCodeValues:
    """
    The purpose or content of the communication is a prescription refill request.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """

    PrescriptionRefillRequest = CommunicationTopicCode("prescription-refill-request")
    """
    The purpose or content of the communication is a progress update.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """
    ProgressUpdate = CommunicationTopicCode("progress-update")
    """
    The purpose or content of the communication is to report labs.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """
    ReportLabs = CommunicationTopicCode("report-labs")
    """
    The purpose or content of the communication is an appointment reminder.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """
    AppointmentReminder = CommunicationTopicCode("appointment-reminder")
    """
    The purpose or content of the communication is a phone consult.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """
    PhoneConsult = CommunicationTopicCode("phone-consult")
    """
    The purpose or content of the communication is a summary report.
    From: http://terminology.hl7.org/CodeSystem/communication-topic in valuesets.xml
    """
    SummaryReport = CommunicationTopicCode("summary-report")
