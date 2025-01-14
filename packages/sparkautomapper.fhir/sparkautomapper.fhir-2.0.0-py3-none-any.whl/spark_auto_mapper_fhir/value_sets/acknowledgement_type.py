from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AcknowledgementType(GenericTypeCode):
    """
    v3.AcknowledgementType
    From: http://terminology.hl7.org/ValueSet/v3-AcknowledgementType in v3-codesystems.xml
         This attribute contains an acknowledgement code as described in the HL7
    message processing rules.  OpenIssue:
    Description was copied from attribute and needs to be improved to be
    appropriate for a code system.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType"


class AcknowledgementTypeValues:
    """
    Receiving application successfully processed message.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """

    ApplicationAcknowledgementAccept = AcknowledgementType("AA")
    """
    Receiving application found error in processing message.  Sending error
    response with additional error detail information.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """
    ApplicationAcknowledgementError = AcknowledgementType("AE")
    """
    Receiving application failed to process message for reason unrelated to
    content or format.  Original message sender must decide on whether to
    automatically send message again.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """
    ApplicationAcknowledgementReject = AcknowledgementType("AR")
    """
    Receiving message handling service accepts responsibility for passing message
    onto receiving application.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """
    AcceptAcknowledgementCommitAccept = AcknowledgementType("CA")
    """
    Receiving message handling service cannot accept message for any other reason
    (e.g. message sequence number, etc.).
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """
    AcceptAcknowledgementCommitError = AcknowledgementType("CE")
    """
    Receiving message handling service rejects message if interaction identifier,
    version or processing mode is incompatible with known receiving application
    role information.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType in v3-codesystems.xml
    """
    AcceptAcknowledgementCommitReject = AcknowledgementType("CR")
