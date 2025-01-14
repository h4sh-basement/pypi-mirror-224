from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.coverageeligibilityrequest import (
    CoverageEligibilityRequestSchema,
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

    # status (FinancialResourceStatusCodes)
    from spark_auto_mapper_fhir.value_sets.financial_resource_status_codes import (
        FinancialResourceStatusCodesCode,
    )

    # priority (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for priority
    from spark_auto_mapper_fhir.value_sets.process_priority_codes import (
        ProcessPriorityCodesCode,
    )

    # End Import for CodeableConcept for priority
    # purpose (EligibilityRequestPurpose)
    from spark_auto_mapper_fhir.value_sets.eligibility_request_purpose import (
        EligibilityRequestPurposeCode,
    )

    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # servicedDate (date)
    # servicedPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # created (dateTime)
    # enterer (Reference)
    # Imports for References for enterer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # provider (Reference)
    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.organization import Organization

    # insurer (Reference)
    # Imports for References for insurer
    # facility (Reference)
    # Imports for References for facility
    from spark_auto_mapper_fhir.resources.location import Location

    # supportingInfo (CoverageEligibilityRequest.SupportingInfo)
    from spark_auto_mapper_fhir.backbone_elements.coverage_eligibility_request_supporting_info import (
        CoverageEligibilityRequestSupportingInfo,
    )

    # insurance (CoverageEligibilityRequest.Insurance)
    from spark_auto_mapper_fhir.backbone_elements.coverage_eligibility_request_insurance import (
        CoverageEligibilityRequestInsurance,
    )

    # item (CoverageEligibilityRequest.Item)
    from spark_auto_mapper_fhir.backbone_elements.coverage_eligibility_request_item import (
        CoverageEligibilityRequestItem,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageEligibilityRequest(FhirResourceBase):
    """
    CoverageEligibilityRequest
    coverageeligibilityrequest.xsd
        The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance details
    of the policy.
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
        identifier: Optional[FhirList[Identifier]] = None,
        status: FinancialResourceStatusCodesCode,
        priority: Optional[CodeableConcept[ProcessPriorityCodesCode]] = None,
        purpose: FhirList[EligibilityRequestPurposeCode],
        patient: Reference[Patient],
        servicedDate: Optional[FhirDate] = None,
        servicedPeriod: Optional[Period] = None,
        created: FhirDateTime,
        enterer: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        provider: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        insurer: Reference[Organization],
        facility: Optional[Reference[Location]] = None,
        supportingInfo: Optional[
            FhirList[CoverageEligibilityRequestSupportingInfo]
        ] = None,
        insurance: Optional[FhirList[CoverageEligibilityRequestInsurance]] = None,
        item: Optional[FhirList[CoverageEligibilityRequestItem]] = None,
    ) -> None:
        """
            The CoverageEligibilityRequest provides patient and insurance coverage
        information to an insurer for them to respond, in the form of an
        CoverageEligibilityResponse, with information regarding whether the stated
        coverage is valid and in-force and optionally to provide the insurance details
        of the policy.
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
            :param identifier: A unique identifier assigned to this coverage eligiblity request.
            :param status: The status of the resource instance.
            :param priority: When the requestor expects the processor to complete processing.
            :param purpose: Code to specify whether requesting: prior authorization requirements for some
        service categories or billing codes; benefits for coverages specified or
        discovered; discovery and return of coverages for the patient; and/or
        validation that the specified coverage is in-force at the date/period
        specified or 'now' if not specified.
            :param patient: The party who is the beneficiary of the supplied coverage and for whom
        eligibility is sought.
            :param servicedDate: None
            :param servicedPeriod: None
            :param created: The date when this resource was created.
            :param enterer: Person who created the request.
            :param provider: The provider which is responsible for the request.
            :param insurer: The Insurer who issued the coverage in question and is the recipient of the
        request.
            :param facility: Facility where the services are intended to be provided.
            :param supportingInfo: Additional information codes regarding exceptions, special considerations, the
        condition, situation, prior or concurrent issues.
            :param insurance: Financial instruments for reimbursement for the health care products and
        services.
            :param item: Service categories or billable services for which benefit details and/or an
        authorization prior to service delivery may be required by the payor.
        """
        super().__init__(
            resourceType="CoverageEligibilityRequest",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            priority=priority,
            purpose=purpose,
            patient=patient,
            servicedDate=servicedDate,
            servicedPeriod=servicedPeriod,
            created=created,
            enterer=enterer,
            provider=provider,
            insurer=insurer,
            facility=facility,
            supportingInfo=supportingInfo,
            insurance=insurance,
            item=item,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return CoverageEligibilityRequestSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
