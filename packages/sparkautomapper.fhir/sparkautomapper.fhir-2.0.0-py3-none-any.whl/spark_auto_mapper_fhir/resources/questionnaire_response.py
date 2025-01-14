from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.questionnaireresponse import (
    QuestionnaireResponseSchema,
)

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # partOf (Reference)
    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.procedure import Procedure

    # questionnaire (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # status (QuestionnaireResponseStatus)
    from spark_auto_mapper_fhir.value_sets.questionnaire_response_status import (
        QuestionnaireResponseStatusCode,
    )

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.resource import Resource

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # authored (dateTime)
    # author (Reference)
    # Imports for References for author
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # source (Reference)
    # Imports for References for source
    # item (QuestionnaireResponse.Item)
    from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item import (
        QuestionnaireResponseItem,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireResponse(FhirResourceBase):
    """
    QuestionnaireResponse
    questionnaireresponse.xsd
        A structured set of questions and their answers. The questions are ordered and
    grouped into coherent subsets, corresponding to the structure of the grouping
    of the questionnaire being responded to.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        basedOn: Optional[FhirList[Reference[Union[CarePlan, ServiceRequest]]]] = None,
        partOf: Optional[FhirList[Reference[Union[Observation, Procedure]]]] = None,
        questionnaire: Optional[FhirCanonical] = None,
        status: QuestionnaireResponseStatusCode,
        subject: Optional[Reference[Resource]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        authored: Optional[FhirDateTime] = None,
        author: Optional[
            Reference[
                Union[
                    Device,
                    Practitioner,
                    PractitionerRole,
                    Patient,
                    RelatedPerson,
                    Organization,
                ]
            ]
        ] = None,
        source: Optional[
            Reference[Union[Patient, Practitioner, PractitionerRole, RelatedPerson]]
        ] = None,
        item: Optional[FhirList[QuestionnaireResponseItem]] = None,
    ) -> None:
        """
            A structured set of questions and their answers. The questions are ordered and
        grouped into coherent subsets, corresponding to the structure of the grouping
        of the questionnaire being responded to.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: A business identifier assigned to a particular completed (or partially
        completed) questionnaire.
            :param basedOn: The order, proposal or plan that is fulfilled in whole or in part by this
        QuestionnaireResponse.  For example, a ServiceRequest seeking an intake
        assessment or a decision support recommendation to assess for post-partum
        depression.
            :param partOf: A procedure or observation that this questionnaire was performed as part of
        the execution of.  For example, the surgery a checklist was executed as part
        of.
            :param questionnaire: The Questionnaire that defines and organizes the questions for which answers
        are being provided.
            :param status: The position of the questionnaire response within its overall lifecycle.
            :param subject: The subject of the questionnaire response.  This could be a patient,
        organization, practitioner, device, etc.  This is who/what the answers apply
        to, but is not necessarily the source of information.
            :param encounter: The Encounter during which this questionnaire response was created or to which
        the creation of this record is tightly associated.
            :param authored: The date and/or time that this set of answers were last changed.
            :param author: Person who received the answers to the questions in the QuestionnaireResponse
        and recorded them in the system.
            :param source: The person who answered the questions about the subject.
            :param item: A group or question item from the original questionnaire for which answers are
        provided.
        """
        super().__init__(
            resourceType="QuestionnaireResponse",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            basedOn=basedOn,
            partOf=partOf,
            questionnaire=questionnaire,
            status=status,
            subject=subject,
            encounter=encounter,
            authored=authored,
            author=author,
            source=source,
            item=item,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return QuestionnaireResponseSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
