from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContainerSeparator(GenericTypeCode):
    """
    v3.ContainerSeparator
    From: http://terminology.hl7.org/ValueSet/v3-ContainerSeparator in v3-codesystems.xml
         A material in a blood collection container that facilites the separation of
    of blood cells from serum or plasma
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ContainerSeparator
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ContainerSeparator"


class ContainerSeparatorValues:
    """
    A gelatinous type of separator material.
    From: http://terminology.hl7.org/CodeSystem/v3-ContainerSeparator in v3-codesystems.xml
    """

    Gel = ContainerSeparator("GEL")
    """
    No separator material is present in the container.
    From: http://terminology.hl7.org/CodeSystem/v3-ContainerSeparator in v3-codesystems.xml
    """
    None_ = ContainerSeparator("NONE")
