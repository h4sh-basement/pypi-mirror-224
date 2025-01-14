from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExposureStateCode(GenericTypeCode):
    """
    ExposureState
    From: http://hl7.org/fhir/exposure-state in valuesets.xml
        Whether the results by exposure is describing the results for the primary
    exposure of interest (exposure) or the alternative state
    (exposureAlternative).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/exposure-state
    """
    codeset: FhirUri = "http://hl7.org/fhir/exposure-state"


class ExposureStateCodeValues:
    """
    used when the results by exposure is describing the results for the primary
    exposure of interest.
    From: http://hl7.org/fhir/exposure-state in valuesets.xml
    """

    Exposure = ExposureStateCode("exposure")
    """
    used when the results by exposure is describing the results for the
    alternative exposure state, control state or comparator state.
    From: http://hl7.org/fhir/exposure-state in valuesets.xml
    """
    ExposureAlternative = ExposureStateCode("exposure-alternative")
