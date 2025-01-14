from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleVisionPrescriptionProductCodesCode(GenericTypeCode):
    """
    ExampleVisionPrescriptionProductCodes
    From: http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct in valuesets.xml
        This value set includes a smattering of Prescription Product codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"
    )


class ExampleVisionPrescriptionProductCodesCodeValues:
    """
    A lens to be fitted to a frame to comprise a pair of glasses.
    From: http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct in valuesets.xml
    """

    Lens = ExampleVisionPrescriptionProductCodesCode("lens")
    """
    A lens to be fitted for wearing directly on an eye.
    From: http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct in valuesets.xml
    """
    ContactLens = ExampleVisionPrescriptionProductCodesCode("contact")
