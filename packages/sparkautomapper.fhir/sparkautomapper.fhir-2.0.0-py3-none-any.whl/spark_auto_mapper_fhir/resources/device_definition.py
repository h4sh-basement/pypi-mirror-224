from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.devicedefinition import DeviceDefinitionSchema

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

    # udiDeviceIdentifier (DeviceDefinition.UdiDeviceIdentifier)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_udi_device_identifier import (
        DeviceDefinitionUdiDeviceIdentifier,
    )

    # manufacturerString (string)
    # manufacturerReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manufacturerReference
    from spark_auto_mapper_fhir.resources.organization import Organization

    # deviceName (DeviceDefinition.DeviceName)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_device_name import (
        DeviceDefinitionDeviceName,
    )

    # modelNumber (string)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.fhir_device_types import FHIRDeviceTypesCode

    # End Import for CodeableConcept for type_
    # specialization (DeviceDefinition.Specialization)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_specialization import (
        DeviceDefinitionSpecialization,
    )

    # version (string)
    # safety (CodeableConcept)
    # Import for CodeableConcept for safety
    from spark_auto_mapper_fhir.value_sets.device_safety import DeviceSafetyCode

    # End Import for CodeableConcept for safety
    # shelfLifeStorage (ProductShelfLife)
    from spark_auto_mapper_fhir.backbone_elements.product_shelf_life import (
        ProductShelfLife,
    )

    # physicalCharacteristics (ProdCharacteristic)
    from spark_auto_mapper_fhir.backbone_elements.prod_characteristic import (
        ProdCharacteristic,
    )

    # languageCode (CodeableConcept)
    # Import for CodeableConcept for languageCode
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for languageCode
    # capability (DeviceDefinition.Capability)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_capability import (
        DeviceDefinitionCapability,
    )

    # property (DeviceDefinition.Property)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_property import (
        DeviceDefinitionProperty,
    )

    # owner (Reference)
    # Imports for References for owner
    # contact (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # url (uri)
    # onlineInformation (uri)
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # parentDevice (Reference)
    # Imports for References for parentDevice
    # material (DeviceDefinition.Material)
    from spark_auto_mapper_fhir.backbone_elements.device_definition_material import (
        DeviceDefinitionMaterial,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceDefinition(FhirResourceBase):
    """
    DeviceDefinition
    devicedefinition.xsd
        The characteristics, operational status and capabilities of a medical-related
    component of a medical device.
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
        udiDeviceIdentifier: Optional[
            FhirList[DeviceDefinitionUdiDeviceIdentifier]
        ] = None,
        manufacturerString: Optional[FhirString] = None,
        manufacturerReference: Optional[Reference[Organization]] = None,
        deviceName: Optional[FhirList[DeviceDefinitionDeviceName]] = None,
        modelNumber: Optional[FhirString] = None,
        type_: Optional[CodeableConcept[FHIRDeviceTypesCode]] = None,
        specialization: Optional[FhirList[DeviceDefinitionSpecialization]] = None,
        version: Optional[FhirList[FhirString]] = None,
        safety: Optional[FhirList[CodeableConcept[DeviceSafetyCode]]] = None,
        shelfLifeStorage: Optional[FhirList[ProductShelfLife]] = None,
        physicalCharacteristics: Optional[ProdCharacteristic] = None,
        languageCode: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        capability: Optional[FhirList[DeviceDefinitionCapability]] = None,
        property: Optional[FhirList[DeviceDefinitionProperty]] = None,
        owner: Optional[Reference[Organization]] = None,
        contact: Optional[FhirList[ContactPoint]] = None,
        url: Optional[FhirUri] = None,
        onlineInformation: Optional[FhirUri] = None,
        note: Optional[FhirList[Annotation]] = None,
        quantity: Optional[Quantity] = None,
        parentDevice: Optional[Reference[DeviceDefinition]] = None,
        material: Optional[FhirList[DeviceDefinitionMaterial]] = None,
    ) -> None:
        """
            The characteristics, operational status and capabilities of a medical-related
        component of a medical device.
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
            :param identifier: Unique instance identifiers assigned to a device by the software,
        manufacturers, other organizations or owners. For example: handle ID.
            :param udiDeviceIdentifier: Unique device identifier (UDI) assigned to device label or package.  Note that
        the Device may include multiple udiCarriers as it either may include just the
        udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
        could have been sold.
            :param manufacturerString: None
            :param manufacturerReference: None
            :param deviceName: A name given to the device to identify it.
            :param modelNumber: The model number for the device.
            :param type_: What kind of device or device system this is.
            :param specialization: The capabilities supported on a  device, the standards to which the device
        conforms for a particular purpose, and used for the communication.
            :param version: The available versions of the device, e.g., software versions.
            :param safety: Safety characteristics of the device.
            :param shelfLifeStorage: Shelf Life and storage information.
            :param physicalCharacteristics: Dimensions, color etc.
            :param languageCode: Language code for the human-readable text strings produced by the device (all
        supported).
            :param capability: Device capabilities.
            :param property: The actual configuration settings of a device as it actually operates, e.g.,
        regulation status, time properties.
            :param owner: An organization that is responsible for the provision and ongoing maintenance
        of the device.
            :param contact: Contact details for an organization or a particular human that is responsible
        for the device.
            :param url: A network address on which the device may be contacted directly.
            :param onlineInformation: Access to on-line information about the device.
            :param note: Descriptive information, usage information or implantation information that is
        not captured in an existing element.
            :param quantity: The quantity of the device present in the packaging (e.g. the number of
        devices present in a pack, or the number of devices in the same package of the
        medicinal product).
            :param parentDevice: The parent device it can be part of.
            :param material: A substance used to create the material(s) of which the device is made.
        """
        super().__init__(
            resourceType="DeviceDefinition",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            udiDeviceIdentifier=udiDeviceIdentifier,
            manufacturerString=manufacturerString,
            manufacturerReference=manufacturerReference,
            deviceName=deviceName,
            modelNumber=modelNumber,
            type_=type_,
            specialization=specialization,
            version=version,
            safety=safety,
            shelfLifeStorage=shelfLifeStorage,
            physicalCharacteristics=physicalCharacteristics,
            languageCode=languageCode,
            capability=capability,
            property=property,
            owner=owner,
            contact=contact,
            url=url,
            onlineInformation=onlineInformation,
            note=note,
            quantity=quantity,
            parentDevice=parentDevice,
            material=material,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return DeviceDefinitionSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
