from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_dns_cname_record import DomainDnsCnameRecord
    from .domain_dns_mx_record import DomainDnsMxRecord
    from .domain_dns_srv_record import DomainDnsSrvRecord
    from .domain_dns_txt_record import DomainDnsTxtRecord
    from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
    from .entity import Entity

from .entity import Entity

@dataclass
class DomainDnsRecord(Entity):
    # If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.
    is_optional: Optional[bool] = None
    # Value used when configuring the name of the DNS record at the DNS host.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, Txt.
    record_type: Optional[str] = None
    # Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
    supported_service: Optional[str] = None
    # Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
    ttl: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsRecord
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsCnameRecord".casefold():
            from .domain_dns_cname_record import DomainDnsCnameRecord

            return DomainDnsCnameRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsMxRecord".casefold():
            from .domain_dns_mx_record import DomainDnsMxRecord

            return DomainDnsMxRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsSrvRecord".casefold():
            from .domain_dns_srv_record import DomainDnsSrvRecord

            return DomainDnsSrvRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsTxtRecord".casefold():
            from .domain_dns_txt_record import DomainDnsTxtRecord

            return DomainDnsTxtRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsUnavailableRecord".casefold():
            from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

            return DomainDnsUnavailableRecord()
        return DomainDnsRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .entity import Entity

        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
            "supportedService": lambda n : setattr(self, 'supported_service', n.get_str_value()),
            "ttl": lambda n : setattr(self, 'ttl', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("label", self.label)
        writer.write_str_value("recordType", self.record_type)
        writer.write_str_value("supportedService", self.supported_service)
        writer.write_int_value("ttl", self.ttl)
    

