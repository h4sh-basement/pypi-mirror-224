from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .json import Json
    from .workbook_filter import WorkbookFilter

from .entity import Entity

@dataclass
class WorkbookTableColumn(Entity):
    # Retrieve the filter applied to the column. Read-only.
    filter: Optional[WorkbookFilter] = None
    # Returns the index number of the column within the columns collection of the table. Zero-indexed. Read-only.
    index: Optional[int] = None
    # Returns the name of the table column.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
    values: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookTableColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTableColumn
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookTableColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .json import Json
        from .workbook_filter import WorkbookFilter

        from .entity import Entity
        from .json import Json
        from .workbook_filter import WorkbookFilter

        fields: Dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(WorkbookFilter)),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_object_value(Json)),
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
        writer.write_object_value("filter", self.filter)
        writer.write_int_value("index", self.index)
        writer.write_str_value("name", self.name)
        writer.write_object_value("values", self.values)
    

