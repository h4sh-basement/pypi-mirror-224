from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..key_value_pair import KeyValuePair
    from .lifecycle_task_category import LifecycleTaskCategory
    from .task_processing_result import TaskProcessingResult

from ..entity import Entity

@dataclass
class Task(Entity):
    # Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.
    arguments: Optional[List[KeyValuePair]] = None
    # The category property
    category: Optional[LifecycleTaskCategory] = None
    # A boolean value that specifies whether, if this task fails, the workflow will stop, and subsequent tasks will not run. Optional.
    continue_on_error: Optional[bool] = None
    # A string that describes the purpose of the task for administrative use. Optional.
    description: Optional[str] = None
    # A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.
    display_name: Optional[str] = None
    # An integer that states in what order the task will run in a workflow.Supports $orderby.
    execution_sequence: Optional[int] = None
    # A boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see supported tasks. Required.Supports $filter(eq, ne).
    task_definition_id: Optional[str] = None
    # The result of processing the task.
    task_processing_results: Optional[List[TaskProcessingResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Task:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Task
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Task()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..key_value_pair import KeyValuePair
        from .lifecycle_task_category import LifecycleTaskCategory
        from .task_processing_result import TaskProcessingResult

        from ..entity import Entity
        from ..key_value_pair import KeyValuePair
        from .lifecycle_task_category import LifecycleTaskCategory
        from .task_processing_result import TaskProcessingResult

        fields: Dict[str, Callable[[Any], None]] = {
            "arguments": lambda n : setattr(self, 'arguments', n.get_collection_of_object_values(KeyValuePair)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LifecycleTaskCategory)),
            "continueOnError": lambda n : setattr(self, 'continue_on_error', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "executionSequence": lambda n : setattr(self, 'execution_sequence', n.get_int_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "taskDefinitionId": lambda n : setattr(self, 'task_definition_id', n.get_str_value()),
            "taskProcessingResults": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(TaskProcessingResult)),
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
        writer.write_collection_of_object_values("arguments", self.arguments)
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("continueOnError", self.continue_on_error)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("executionSequence", self.execution_sequence)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("taskDefinitionId", self.task_definition_id)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
    

