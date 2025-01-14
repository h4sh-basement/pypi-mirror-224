from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConstraintSeverityCode(GenericTypeCode):
    """
    ConstraintSeverity
    From: http://hl7.org/fhir/constraint-severity in valuesets.xml
        SHALL applications comply with this constraint?
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/constraint-severity
    """
    codeset: FhirUri = "http://hl7.org/fhir/constraint-severity"


class ConstraintSeverityCodeValues:
    """
    If the constraint is violated, the resource is not conformant.
    From: http://hl7.org/fhir/constraint-severity in valuesets.xml
    """

    Error = ConstraintSeverityCode("error")
    """
    If the constraint is violated, the resource is conformant, but it is not
    necessarily following best practice.
    From: http://hl7.org/fhir/constraint-severity in valuesets.xml
    """
    Warning = ConstraintSeverityCode("warning")
