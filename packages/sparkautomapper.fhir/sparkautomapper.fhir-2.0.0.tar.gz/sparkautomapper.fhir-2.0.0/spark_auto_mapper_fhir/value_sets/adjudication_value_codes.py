from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdjudicationValueCodesCode(GenericTypeCode):
    """
    AdjudicationValueCodes
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
        This value set includes a smattering of Adjudication Value codes which
    includes codes to indicate the amounts eligible under the plan, the amount of
    benefit, copays etc.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/adjudication
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/adjudication"


class AdjudicationValueCodesCodeValues:
    """
    The total submitted amount for the claim or group or line item.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """

    SubmittedAmount = AdjudicationValueCodesCode("submitted")
    """
    Patient Co-Payment
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    CoPay = AdjudicationValueCodesCode("copay")
    """
    Amount of the change which is considered for adjudication.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    EligibleAmount = AdjudicationValueCodesCode("eligible")
    """
    Amount deducted from the eligible amount prior to adjudication.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    Deductible = AdjudicationValueCodesCode("deductible")
    """
    The amount of deductible which could not allocated to other line items.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    UnallocatedDeductible = AdjudicationValueCodesCode("unallocdeduct")
    """
    Eligible Percentage.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    Eligible_ = AdjudicationValueCodesCode("eligpercent")
    """
    The amount of tax.
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    Tax = AdjudicationValueCodesCode("tax")
    """
    Amount payable under the coverage
    From: http://terminology.hl7.org/CodeSystem/adjudication in valuesets.xml
    """
    BenefitAmount = AdjudicationValueCodesCode("benefit")
