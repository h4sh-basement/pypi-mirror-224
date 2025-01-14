from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenContainedPreferenceCode(GenericTypeCode):
    """
    SpecimenContainedPreference
    From: http://hl7.org/fhir/specimen-contained-preference in valuesets.xml
        Degree of preference of a type of conditioned specimen.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/specimen-contained-preference
    """
    codeset: FhirUri = "http://hl7.org/fhir/specimen-contained-preference"


class SpecimenContainedPreferenceCodeValues:
    """
    This type of contained specimen is preferred to collect this kind of specimen.
    From: http://hl7.org/fhir/specimen-contained-preference in valuesets.xml
    """

    Preferred = SpecimenContainedPreferenceCode("preferred")
    """
    This type of conditioned specimen is an alternate.
    From: http://hl7.org/fhir/specimen-contained-preference in valuesets.xml
    """
    Alternate = SpecimenContainedPreferenceCode("alternate")
