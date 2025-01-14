from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RequestResourceTypeCode(GenericTypeCode):
    """
    RequestResourceType
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
        A list of all the request resource types defined in this version of the FHIR
    specification.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/request-resource-types
    """
    codeset: FhirUri = "http://hl7.org/fhir/request-resource-types"


class RequestResourceTypeCodeValues:
    """
    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one or
    more Encounter(s).
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """

    Appointment = RequestResourceTypeCode("Appointment")
    """
    A reply to an appointment request for a patient and/or practitioner(s), such
    as a confirmation or rejection.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    AppointmentResponse = RequestResourceTypeCode("AppointmentResponse")
    """
    Healthcare plan for patient or group.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    CarePlan = RequestResourceTypeCode("CarePlan")
    """
    Claim, Pre-determination or Pre-authorization.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    Claim = RequestResourceTypeCode("Claim")
    """
    A request for information to be sent to a receiver.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    CommunicationRequest = RequestResourceTypeCode("CommunicationRequest")
    """
    Legal Agreement.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    Contract = RequestResourceTypeCode("Contract")
    """
    Medical device request.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    DeviceRequest = RequestResourceTypeCode("DeviceRequest")
    """
    Enrollment request.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    EnrollmentRequest = RequestResourceTypeCode("EnrollmentRequest")
    """
    Guidance or advice relating to an immunization.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    ImmunizationRecommendation = RequestResourceTypeCode("ImmunizationRecommendation")
    """
    Ordering of medication for patient or group.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    MedicationRequest = RequestResourceTypeCode("MedicationRequest")
    """
    Diet, formula or nutritional supplement request.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    NutritionOrder = RequestResourceTypeCode("NutritionOrder")
    """
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    ServiceRequest = RequestResourceTypeCode("ServiceRequest")
    """
    Request for a medication, substance or device.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    SupplyRequest = RequestResourceTypeCode("SupplyRequest")
    """
    A task to be performed.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    Task = RequestResourceTypeCode("Task")
    """
    Prescription for vision correction products for a patient.
    From: http://hl7.org/fhir/request-resource-types in valuesets.xml
    """
    VisionPrescription = RequestResourceTypeCode("VisionPrescription")
