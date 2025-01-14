from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Hl7V3Conformance(GenericTypeCode):
    """
    v3.hl7V3Conformance
    From: http://terminology.hl7.org/ValueSet/v3-hl7V3Conformance in v3-codesystems.xml
          Description:
    Identifies allowed codes for HL7aTMs v3 conformance property.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance"


class Hl7V3ConformanceValues:
    """
    Description: Implementers receiving this property must not raise an error if
    the data is received, but will not perform any useful function with the data.
    This conformance level is not used in profiles or other artifacts that are
    specific to the "sender" or "initiator" of a communication.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """

    Ignored = Hl7V3Conformance("I")
    """
    Description: All implementers are prohibited from transmitting this content,
    and may raise an error if they receive it.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """
    NotPermitted = Hl7V3Conformance("NP")
    """
    Description: All implementers must support this property.  I.e. they must be
    able to transmit, or to receive and usefully handle the concept.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """
    Required = Hl7V3Conformance("R")
    """
    Description: The element is considered "required" (i.e. must be supported)
    from the perspective of systems that consume  instances, but is "undetermined"
    for systems that generate instances.  Used only as part of specifications that
    define both initiator and consumer expectations.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """
    RequiredForConsumer = Hl7V3Conformance("RC")
    """
    Description: The element is considered "required" (i.e. must be supported)
    from the perspective of systems that generate instances, but is "undetermined"
    for systems that consume instances.  Used only as part of specifications that
    define both initiator and consumer expectations.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """
    RequiredForInitiator = Hl7V3Conformance("RI")
    """
    Description: The conformance expectations for this element have not yet been
    determined.
    From: http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance in v3-codesystems.xml
    """
    Undetermined = Hl7V3Conformance("U")
