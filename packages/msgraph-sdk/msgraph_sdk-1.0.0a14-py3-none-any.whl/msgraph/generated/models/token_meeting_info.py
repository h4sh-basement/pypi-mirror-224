from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_info import MeetingInfo

from .meeting_info import MeetingInfo

@dataclass
class TokenMeetingInfo(MeetingInfo):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.tokenMeetingInfo"
    # The token used to join the call.
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TokenMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TokenMeetingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TokenMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_info import MeetingInfo

        from .meeting_info import MeetingInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("token", self.token)
    

