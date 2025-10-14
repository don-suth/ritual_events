from base_event import BaseEvent
from typing import Literal
from pydantic import TypeAdapter, ValidationError


class AuthenticateEvent(BaseEvent):
	action: Literal["Authenticate"] = "Authenticate"
	token: str

class OpenDoorEvent(BaseEvent):
	action: Literal["OpenDoor"] = "OpenDoor"

class CloseDoorEvent(BaseEvent):
	action: Literal["CloseDoor"] = "CloseDoor"


supported_from_phantasm_events = (
	AuthenticateEvent
	| OpenDoorEvent
	| CloseDoorEvent
)
from_phantasm_adapter = TypeAdapter(supported_from_phantasm_events)

def validate_from_phantasm_event(raw_event, action_is_mandatory=True):
	try:
		event = from_phantasm_adapter.validate_python(raw_event, context={"action_is_mandatory": action_is_mandatory})
	except ValidationError:
		event = None
	return event
