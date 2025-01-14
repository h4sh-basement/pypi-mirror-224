from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractSubtypeCodesCode(GenericTypeCode):
    """
    ContractSubtypeCodes
    From: http://terminology.hl7.org/CodeSystem/contractsubtypecodes in valuesets.xml
        This value set includes sample Contract Subtype codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/contractsubtypecodes
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/contractsubtypecodes"


class ContractSubtypeCodesCodeValues:
    """
    Canadian health information disclosure policy.
    From: http://terminology.hl7.org/CodeSystem/contractsubtypecodes in valuesets.xml
    """

    Disclosure_CA = ContractSubtypeCodesCode("disclosure-ca")
    """
    United States health information disclosure policy.
    From: http://terminology.hl7.org/CodeSystem/contractsubtypecodes in valuesets.xml
    """
    Disclosure_US = ContractSubtypeCodesCode("disclosure-us")
