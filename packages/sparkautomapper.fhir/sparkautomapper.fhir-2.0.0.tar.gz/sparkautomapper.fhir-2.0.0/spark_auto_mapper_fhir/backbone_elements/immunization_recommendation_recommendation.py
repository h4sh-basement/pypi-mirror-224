from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # vaccineCode (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for vaccineCode
    # Import for CodeableConcept for vaccineCode
    from spark_auto_mapper_fhir.value_sets.vaccine_administered_value_set import (
        VaccineAdministeredValueSetCode,
    )

    # End Import for CodeableConcept for vaccineCode
    # targetDisease (CodeableConcept)
    # End Import for References for targetDisease
    # Import for CodeableConcept for targetDisease
    from spark_auto_mapper_fhir.value_sets.immunization_recommendation_target_disease_codes import (
        ImmunizationRecommendationTargetDiseaseCodesCode,
    )

    # End Import for CodeableConcept for targetDisease
    # contraindicatedVaccineCode (CodeableConcept)
    # End Import for References for contraindicatedVaccineCode
    # Import for CodeableConcept for contraindicatedVaccineCode
    # End Import for CodeableConcept for contraindicatedVaccineCode
    # forecastStatus (CodeableConcept)
    # End Import for References for forecastStatus
    # Import for CodeableConcept for forecastStatus
    from spark_auto_mapper_fhir.value_sets.immunization_recommendation_status_codes import (
        ImmunizationRecommendationStatusCodesCode,
    )

    # End Import for CodeableConcept for forecastStatus
    # forecastReason (CodeableConcept)
    # End Import for References for forecastReason
    # Import for CodeableConcept for forecastReason
    from spark_auto_mapper_fhir.value_sets.immunization_recommendation_reason_codes import (
        ImmunizationRecommendationReasonCodesCode,
    )

    # End Import for CodeableConcept for forecastReason
    # dateCriterion (ImmunizationRecommendation.DateCriterion)
    from spark_auto_mapper_fhir.backbone_elements.immunization_recommendation_date_criterion import (
        ImmunizationRecommendationDateCriterion,
    )

    # description (string)
    # series (string)
    # doseNumberPositiveInt (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # doseNumberString (string)
    # seriesDosesPositiveInt (positiveInt)
    # seriesDosesString (string)
    # supportingImmunization (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for supportingImmunization
    from spark_auto_mapper_fhir.resources.immunization import Immunization
    from spark_auto_mapper_fhir.resources.immunization_evaluation import (
        ImmunizationEvaluation,
    )

    # supportingPatientInformation (Reference)
    # Imports for References for supportingPatientInformation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationRecommendationRecommendation(FhirBackboneElementBase):
    """
    ImmunizationRecommendation.Recommendation
        A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        vaccineCode: Optional[
            FhirList[CodeableConcept[VaccineAdministeredValueSetCode]]
        ] = None,
        targetDisease: Optional[
            CodeableConcept[ImmunizationRecommendationTargetDiseaseCodesCode]
        ] = None,
        contraindicatedVaccineCode: Optional[
            FhirList[CodeableConcept[VaccineAdministeredValueSetCode]]
        ] = None,
        forecastStatus: CodeableConcept[ImmunizationRecommendationStatusCodesCode],
        forecastReason: Optional[
            FhirList[CodeableConcept[ImmunizationRecommendationReasonCodesCode]]
        ] = None,
        dateCriterion: Optional[
            FhirList[ImmunizationRecommendationDateCriterion]
        ] = None,
        description: Optional[FhirString] = None,
        series: Optional[FhirString] = None,
        doseNumberPositiveInt: Optional[FhirPositiveInt] = None,
        doseNumberString: Optional[FhirString] = None,
        seriesDosesPositiveInt: Optional[FhirPositiveInt] = None,
        seriesDosesString: Optional[FhirString] = None,
        supportingImmunization: Optional[
            FhirList[Reference[Union[Immunization, ImmunizationEvaluation]]]
        ] = None,
        supportingPatientInformation: Optional[FhirList[Reference[Resource]]] = None,
    ) -> None:
        """
            A patient's point-in-time set of recommendations (i.e. forecasting) according
        to a published schedule with optional supporting justification.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param vaccineCode: Vaccine(s) or vaccine group that pertain to the recommendation.
            :param targetDisease: The targeted disease for the recommendation.
            :param contraindicatedVaccineCode: Vaccine(s) which should not be used to fulfill the recommendation.
            :param forecastStatus: Indicates the patient status with respect to the path to immunity for the
        target disease.
            :param forecastReason: The reason for the assigned forecast status.
            :param dateCriterion: Vaccine date recommendations.  For example, earliest date to administer,
        latest date to administer, etc.
            :param description: Contains the description about the protocol under which the vaccine was
        administered.
            :param series: One possible path to achieve presumed immunity against a disease - within the
        context of an authority.
            :param doseNumberPositiveInt: None
            :param doseNumberString: None
            :param seriesDosesPositiveInt: None
            :param seriesDosesString: None
            :param supportingImmunization: Immunization event history and/or evaluation that supports the status and
        recommendation.
            :param supportingPatientInformation: Patient Information that supports the status and recommendation.  This
        includes patient observations, adverse reactions and allergy/intolerance
        information.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            vaccineCode=vaccineCode,
            targetDisease=targetDisease,
            contraindicatedVaccineCode=contraindicatedVaccineCode,
            forecastStatus=forecastStatus,
            forecastReason=forecastReason,
            dateCriterion=dateCriterion,
            description=description,
            series=series,
            doseNumberPositiveInt=doseNumberPositiveInt,
            doseNumberString=doseNumberString,
            seriesDosesPositiveInt=seriesDosesPositiveInt,
            seriesDosesString=seriesDosesString,
            supportingImmunization=supportingImmunization,
            supportingPatientInformation=supportingPatientInformation,
        )
