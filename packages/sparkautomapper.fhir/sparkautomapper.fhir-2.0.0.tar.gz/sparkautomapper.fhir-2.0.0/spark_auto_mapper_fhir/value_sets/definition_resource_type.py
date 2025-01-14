from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DefinitionResourceTypeCode(GenericTypeCode):
    """
    DefinitionResourceType
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
        A list of all the definition resource types defined in this version of the
    FHIR specification.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/definition-resource-types
    """
    codeset: FhirUri = "http://hl7.org/fhir/definition-resource-types"


class DefinitionResourceTypeCodeValues:
    """
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """

    ActivityDefinition = DefinitionResourceTypeCode("ActivityDefinition")
    """
    The EventDefinition resource provides a reusable description of when a
    particular event can occur.
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """
    EventDefinition = DefinitionResourceTypeCode("EventDefinition")
    """
    The Measure resource provides the definition of a quality measure.
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """
    Measure = DefinitionResourceTypeCode("Measure")
    """
    A formal computable definition of an operation (on the RESTful interface) or a
    named query (using the search interaction).
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """
    OperationDefinition = DefinitionResourceTypeCode("OperationDefinition")
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general enough
    to support the description of a broad range of clinical artifacts such as
    clinical decision support rules, order sets and protocols.
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """
    PlanDefinition = DefinitionResourceTypeCode("PlanDefinition")
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
    From: http://hl7.org/fhir/definition-resource-types in valuesets.xml
    """
    Questionnaire = DefinitionResourceTypeCode("Questionnaire")
