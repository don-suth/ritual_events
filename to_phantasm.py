from datetime import datetime
from pydantic import TypeAdapter, ValidationError
from pydantic_extra_types.color import Color as Colour
from typing import Literal
from .base_event import BaseEvent

entrances = Literal["Tav", "Guild"]


class LetMeInEvent(BaseEvent):
	action: Literal["LetMeIn"] = "LetMeIn"
	name: str
	entrance: entrances


class FoodRunEvent(BaseEvent):
	action: Literal["FoodRun"] = "FoodRun"
	arrival_time: datetime
	entrance: entrances


class UpdateClockSettingsEvent(BaseEvent):
	action: Literal["ClockSettingsUpdate"] = "ClockSettingsUpdate"
	new_brightness: int | None = None
	new_text_colour: Colour | None = None
	alternate_seconds: bool | None = None


class OpenDoorEvent(BaseEvent):
	action: Literal["OpenDoor"] = "OpenDoor"


class CloseDoorEvent(BaseEvent):
	action: Literal["CloseDoor"] = "CloseDoor"


supported_to_phantasm_events = (
	LetMeInEvent
	| FoodRunEvent
	| UpdateClockSettingsEvent
	| OpenDoorEvent
	| CloseDoorEvent
)
to_phantasm_adapter = TypeAdapter(supported_to_phantasm_events)


def validate_to_phantasm(python_event, action_is_mandatory=True):
	try:
		event = to_phantasm_adapter.validate_python(python_event, context={"action_is_mandatory": action_is_mandatory})
	except ValidationError:
		event = None
	return event


def validate_to_phantasm_json(json_event, action_is_mandatory=True):
	try:
		event = to_phantasm_adapter.validate_json(json_event, context={"action_is_mandatory": action_is_mandatory})
	except ValidationError:
		event = None
	return event
