from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .user_account import UserAccount

from .alert_evidence import AlertEvidence

@dataclass
class MailboxEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.mailboxEvidence"
    # The name associated with the mailbox.
    display_name: Optional[str] = None
    # The primary email address of the mailbox.
    primary_address: Optional[str] = None
    # The user account of the mailbox.
    user_account: Optional[UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailboxEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MailboxEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .user_account import UserAccount

        from .alert_evidence import AlertEvidence
        from .user_account import UserAccount

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "primaryAddress": lambda n : setattr(self, 'primary_address', n.get_str_value()),
            "userAccount": lambda n : setattr(self, 'user_account', n.get_object_value(UserAccount)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("primaryAddress", self.primary_address)
        writer.write_object_value("userAccount", self.user_account)
    

