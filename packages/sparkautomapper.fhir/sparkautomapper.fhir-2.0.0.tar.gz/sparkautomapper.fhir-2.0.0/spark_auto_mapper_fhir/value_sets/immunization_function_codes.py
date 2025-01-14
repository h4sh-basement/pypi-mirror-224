from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationFunctionCodesCode(GenericTypeCode):
    """
    ImmunizationFunctionCodes
    From: http://hl7.org/fhir/ValueSet/immunization-function in valuesets.xml
        The value set to instantiate this attribute should be drawn from a
    terminologically robust code system that consists of or contains concepts to
    support describing the function a practitioner or organization may play in the
    immunization event. This value set is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v2-0443
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v2-0443"


class ImmunizationFunctionCodesCodeValues:
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """

    Admitting = ImmunizationFunctionCodesCode("AD")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    Assistant_AlternateInterpreter = ImmunizationFunctionCodesCode("AI")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    AdministeringProvider = ImmunizationFunctionCodesCode("AP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    Attending = ImmunizationFunctionCodesCode("AT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    CollectingProvider = ImmunizationFunctionCodesCode("CLP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    ConsultingProvider = ImmunizationFunctionCodesCode("CP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    DispensingProvider = ImmunizationFunctionCodesCode("DP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    EnteringProvider_probablyNotTheSameAsTranscriptionist_ = (
        ImmunizationFunctionCodesCode("EP")
    )
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    FamilyHealthCareProfessional = ImmunizationFunctionCodesCode("FHCP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    InitiatingProvider_asInActionBy_ = ImmunizationFunctionCodesCode("IP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    MedicalDirector = ImmunizationFunctionCodesCode("MDIR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    OrderingProvider = ImmunizationFunctionCodesCode("OP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    Pharmacist_notSureHowToDissectPharmacist_TreatmentSupplier_sVerifierID_ = (
        ImmunizationFunctionCodesCode("PH")
    )
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    PrimaryInterpreter = ImmunizationFunctionCodesCode("PI")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    PrimaryCareProvider = ImmunizationFunctionCodesCode("PP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    ResponsibleObserver = ImmunizationFunctionCodesCode("RO")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    ReferringProvider = ImmunizationFunctionCodesCode("RP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    ReferredToProvider = ImmunizationFunctionCodesCode("RT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    Technician = ImmunizationFunctionCodesCode("TN")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    Transcriptionist = ImmunizationFunctionCodesCode("TR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    VerifyingProvider = ImmunizationFunctionCodesCode("VP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    VerifyingPharmaceuticalSupplier_notSureHowToDissectPharmacist_TreatmentSupplier_sVerifierID_ = ImmunizationFunctionCodesCode(
        "VPS"
    )
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0443 in v2-tables.xml
    """
    VerifyingTreatmentSupplier_notSureHowToDissectPharmacist_TreatmentSupplier_sVerifierID_ = ImmunizationFunctionCodesCode(
        "VTS"
    )
    """
    From: http://hl7.org/fhir/ValueSet/immunization-function in valuesets.xml
    """
    OP = ImmunizationFunctionCodesCode("OP")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-function in valuesets.xml
    """
    AP = ImmunizationFunctionCodesCode("AP")
