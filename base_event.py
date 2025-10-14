from pydantic import BaseModel, ValidationInfo, Field
from datetime import datetime

class BaseEvent(BaseModel):
	"""
	Base Class for events.
	tl;dr: This code means:
		- Generating models allows the default action value by default.
		- You can set "action_is_mandatory" in the context to ensure that the action is required for validation.

	Examples:
		>>> new_event = {"event_time": "1760408388", "arrival_time": 1760408388, "entrance": "Guild"}
			# ^ Note the missing "action" field.
		>>> LetMeInEvent.model_validate(new_event)
		FoodRunEvent(event_time=<...>, action='FoodRun', arrival_time=<...>, entrance='Guild')
			# ^ This works, because "action" has a default value of "LetMeIn"
		>>> LetMeInEvent.model_validate(new_event, context={"action_is_mandatory": True})
			# This raises a Validation Error, since "action" was not provided and is now mandatory.
	"""
	
	@model_validator(mode="after")
	def validate_action_is_mandatory(self, info: ValidationInfo):
		if isinstance(info.context, dict) and info.context.get("action_is_mandatory"):
			if "action" not in self.model_fields_set:
				raise ValueError("action not set when 'action_is_mandatory' is True")
		return self
	
	event_time: datetime = Field(default_factory=datetime.now)