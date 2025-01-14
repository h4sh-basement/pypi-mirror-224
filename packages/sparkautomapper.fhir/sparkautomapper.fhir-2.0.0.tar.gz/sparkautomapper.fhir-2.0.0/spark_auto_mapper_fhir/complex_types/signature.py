from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_fhir_schemas.r4.complex_types.signature import SignatureSchema


if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # type_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.signature_type_codes import (
        SignatureTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # when (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # who (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for who
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization

    # onBehalfOf (Reference)
    # Imports for References for onBehalfOf
    # targetFormat (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # sigFormat (Mime Types)
    # data (base64Binary)
    from spark_auto_mapper_fhir.fhir_types.base64_binary import FhirBase64Binary


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Signature(FhirComplexTypeBase):
    """
    Signature
    fhir-base.xsd
        A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[NestedExtensionItem]] = None,
        type_: FhirList[Coding[SignatureTypeCodesCode]],
        when: FhirInstant,
        who: Reference[
            Union[
                Practitioner,
                PractitionerRole,
                RelatedPerson,
                Patient,
                Device,
                Organization,
            ]
        ],
        onBehalfOf: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    RelatedPerson,
                    Patient,
                    Device,
                    Organization,
                ]
            ]
        ] = None,
        targetFormat: Optional[MimeTypesCode] = None,
        sigFormat: Optional[MimeTypesCode] = None,
        data: Optional[FhirBase64Binary] = None,
    ) -> None:
        """
            A signature along with supporting context. The signature may be a digital
        signature that is cryptographic in nature, or some other signature acceptable
        to the domain. This other signature may be as simple as a graphical image
        representing a hand-written signature, or a signature ceremony Different
        signature approaches have different utilities.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param type_: An indication of the reason that the entity signed this document. This may be
        explicitly included as part of the signature information and can be used when
        determining accountability for various actions concerning the document.
            :param when: When the digital signature was signed.
            :param who: A reference to an application-usable description of the identity that signed
        (e.g. the signature used their private key).
            :param onBehalfOf: A reference to an application-usable description of the identity that is
        represented by the signature.
            :param targetFormat: A mime type that indicates the technical format of the target resources signed
        by the signature.
            :param sigFormat: A mime type that indicates the technical format of the signature. Important
        mime types are application/signature+xml for X ML DigSig, application/jose for
        JWS, and image/* for a graphical image of a signature, etc.
            :param data: The base64 encoding of the Signature content. When signature is not recorded
        electronically this element would be empty.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            when=when,
            who=who,
            onBehalfOf=onBehalfOf,
            targetFormat=targetFormat,
            sigFormat=sigFormat,
            data=data,
        )
        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return SignatureSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
