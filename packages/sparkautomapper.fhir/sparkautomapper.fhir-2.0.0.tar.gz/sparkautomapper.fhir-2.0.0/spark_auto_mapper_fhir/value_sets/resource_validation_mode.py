from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResourceValidationModeCode(GenericTypeCode):
    """
    ResourceValidationMode
    From: http://hl7.org/fhir/resource-validation-mode in valuesets.xml
        Codes indicating the type of validation to perform.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/resource-validation-mode
    """
    codeset: FhirUri = "http://hl7.org/fhir/resource-validation-mode"


class ResourceValidationModeCodeValues:
    """
    The server checks the content, and then checks that the content would be
    acceptable as a create (e.g. that the content would not violate any uniqueness
    constraints).
    From: http://hl7.org/fhir/resource-validation-mode in valuesets.xml
    """

    ValidateForCreate = ResourceValidationModeCode("create")
    """
    The server checks the content, and then checks that it would accept it as an
    update against the nominated specific resource (e.g. that there are no changes
    to immutable fields the server does not allow to change and checking version
    integrity if appropriate).
    From: http://hl7.org/fhir/resource-validation-mode in valuesets.xml
    """
    ValidateForUpdate = ResourceValidationModeCode("update")
    """
    The server ignores the content and checks that the nominated resource is
    allowed to be deleted (e.g. checking referential integrity rules).
    From: http://hl7.org/fhir/resource-validation-mode in valuesets.xml
    """
    ValidateForDelete = ResourceValidationModeCode("delete")
    """
    The server checks an existing resource (must be nominated by id, not provided
    as a parameter) as valid against the nominated profile.
    From: http://hl7.org/fhir/resource-validation-mode in valuesets.xml
    """
    ValidateAgainstAProfile = ResourceValidationModeCode("profile")
