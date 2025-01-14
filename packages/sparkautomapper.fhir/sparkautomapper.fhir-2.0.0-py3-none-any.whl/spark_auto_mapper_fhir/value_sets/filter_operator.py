from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FilterOperatorCode(GenericTypeCode):
    """
    FilterOperator
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
        The kind of operation to perform as a part of a property based filter.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/filter-operator
    """
    codeset: FhirUri = "http://hl7.org/fhir/filter-operator"


class FilterOperatorCodeValues:
    """
    The specified property of the code equals the provided value.
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """

    Equals = FilterOperatorCode("=")
    """
    Includes all concept ids that have a transitive is-a relationship with the
    concept Id provided as the value, including the provided concept itself
    (include descendant codes and self).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    IsA_bySubsumption_ = FilterOperatorCode("is-a")
    """
    Includes all concept ids that have a transitive is-a relationship with the
    concept Id provided as the value, excluding the provided concept itself i.e.
    include descendant codes only).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    DescendentOf_bySubsumption_ = FilterOperatorCode("descendent-of")
    """
    The specified property of the code does not have an is-a relationship with the
    provided value.
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    Not_IsA_bySubsumption_ = FilterOperatorCode("is-not-a")
    """
    The specified property of the code  matches the regex specified in the
    provided value.
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    RegularExpression = FilterOperatorCode("regex")
    """
    The specified property of the code is in the set of codes or concepts
    specified in the provided value (comma separated list).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    InSet = FilterOperatorCode("in")
    """
    The specified property of the code is not in the set of codes or concepts
    specified in the provided value (comma separated list).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    NotInSet = FilterOperatorCode("not-in")
    """
    Includes all concept ids that have a transitive is-a relationship from the
    concept Id provided as the value, including the provided concept itself (i.e.
    include ancestor codes and self).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    Generalizes_bySubsumption_ = FilterOperatorCode("generalizes")
    """
    The specified property of the code has at least one value (if the specified
    value is true; if the specified value is false, then matches when the
    specified property of the code has no values).
    From: http://hl7.org/fhir/filter-operator in valuesets.xml
    """
    Exists = FilterOperatorCode("exists")
