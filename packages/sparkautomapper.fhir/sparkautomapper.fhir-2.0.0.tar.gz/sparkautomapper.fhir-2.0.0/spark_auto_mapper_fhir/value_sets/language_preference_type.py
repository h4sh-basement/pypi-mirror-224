from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class LanguagePreferenceTypeCode(GenericTypeCode):
    """
    LanguagePreferenceType
    From: http://hl7.org/fhir/language-preference-type in valuesets.xml
        This value set defines the set of codes for describing the type or mode of the
    patient's preferred language.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/language-preference-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/language-preference-type"


class LanguagePreferenceTypeCodeValues:
    """
    The patient prefers to verbally communicate with the associated language.
    From: http://hl7.org/fhir/language-preference-type in valuesets.xml
    """

    Verbal = LanguagePreferenceTypeCode("verbal")
    """
    The patient prefers to communicate in writing with the associated language.
    From: http://hl7.org/fhir/language-preference-type in valuesets.xml
    """
    Written = LanguagePreferenceTypeCode("written")
