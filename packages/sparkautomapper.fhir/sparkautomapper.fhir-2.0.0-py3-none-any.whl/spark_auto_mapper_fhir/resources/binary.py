from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.binary import BinarySchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # contentType (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # securityContext (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for securityContext
    from spark_auto_mapper_fhir.resources.resource import Resource

    # data (base64Binary)
    from spark_auto_mapper_fhir.fhir_types.base64_binary import FhirBase64Binary


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Binary(FhirResourceBase):
    """
    Binary
    binary.xsd
        A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
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
        contentType: MimeTypesCode,
        securityContext: Optional[Reference[Resource]] = None,
        data: Optional[FhirBase64Binary] = None,
    ) -> None:
        """
            A resource that represents the data of a single raw artifact as digital
        content accessible in its native format.  A Binary resource can contain any
        content, whether text, image, pdf, zip archive, etc.
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
            :param contentType: MimeType of the binary content represented as a standard MimeType (BCP 13).
            :param securityContext: This element identifies another resource that can be used as a proxy of the
        security sensitivity to use when deciding and enforcing access control rules
        for the Binary resource. Given that the Binary resource contains very few
        elements that can be used to determine the sensitivity of the data and
        relationships to individuals, the referenced resource stands in as a proxy
        equivalent for this purpose. This referenced resource may be related to the
        Binary (e.g. Media, DocumentReference), or may be some non-related Resource
        purely as a security proxy. E.g. to identify that the binary resource relates
        to a patient, and access should only be granted to applications that have
        access to the patient.
            :param data: The actual content, base64 encoded.
        """
        super().__init__(
            resourceType="Binary",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            contentType=contentType,
            securityContext=securityContext,
            data=data,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return BinarySchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
