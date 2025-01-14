from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # issued (dateTime)
    # applies (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # topicCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for topicCodeableConcept
    # Import for CodeableConcept for topicCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for topicCodeableConcept
    # topicReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for topicReference
    # type_ (CodeableConcept)
    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.contract_term_type_codes import (
        ContractTermTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # subType (CodeableConcept)
    # End Import for References for subType
    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.contract_term_subtype_codes import (
        ContractTermSubtypeCodesCode,
    )

    # End Import for CodeableConcept for subType
    # text (string)
    # securityLabel (Contract.SecurityLabel)
    from spark_auto_mapper_fhir.backbone_elements.contract_security_label import (
        ContractSecurityLabel,
    )

    # offer (Contract.Offer)
    from spark_auto_mapper_fhir.backbone_elements.contract_offer import ContractOffer

    # asset (Contract.Asset)
    from spark_auto_mapper_fhir.backbone_elements.contract_asset import ContractAsset

    # action (Contract.Action)
    from spark_auto_mapper_fhir.backbone_elements.contract_action import ContractAction


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractTerm(FhirBackboneElementBase):
    """
    Contract.Term
        Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        issued: Optional[FhirDateTime] = None,
        applies: Optional[Period] = None,
        topicCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        topicReference: Optional[Reference[Resource]] = None,
        type_: Optional[CodeableConcept[ContractTermTypeCodesCode]] = None,
        subType: Optional[CodeableConcept[ContractTermSubtypeCodesCode]] = None,
        text: Optional[FhirString] = None,
        securityLabel: Optional[FhirList[ContractSecurityLabel]] = None,
        offer: ContractOffer,
        asset: Optional[FhirList[ContractAsset]] = None,
        action: Optional[FhirList[ContractAction]] = None,
        group: Optional[FhirList[ContractTerm]] = None,
    ) -> None:
        """
            Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.

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
            :param identifier: Unique identifier for this particular Contract Provision.
            :param issued: When this Contract Provision was issued.
            :param applies: Relevant time or time-period when this Contract Provision is applicable.
            :param topicCodeableConcept: None
            :param topicReference: None
            :param type_: A legal clause or condition contained within a contract that requires one or
        both parties to perform a particular requirement by some specified time or
        prevents one or both parties from performing a particular requirement by some
        specified time.
            :param subType: A specialized legal clause or condition based on overarching contract type.
            :param text: Statement of a provision in a policy or a contract.
            :param securityLabel: Security labels that protect the handling of information about the term and
        its elements, which may be specifically identified..
            :param offer: The matter of concern in the context of this provision of the agrement.
            :param asset: Contract Term Asset List.
            :param action: An actor taking a role in an activity for which it can be assigned some degree
        of responsibility for the activity taking place.
            :param group: Nested group of Contract Provisions.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            issued=issued,
            applies=applies,
            topicCodeableConcept=topicCodeableConcept,
            topicReference=topicReference,
            type_=type_,
            subType=subType,
            text=text,
            securityLabel=securityLabel,
            offer=offer,
            asset=asset,
            action=action,
            group=group,
        )
