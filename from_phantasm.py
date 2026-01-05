from .base_event import BaseEvent
from typing import Literal
from pydantic import TypeAdapter, ValidationError


class AuthenticateEvent(BaseEvent):
	action: Literal["Authenticate"] = "Authenticate"
	token: str


supported_from_phantasm_events = (
	AuthenticateEvent
)
from_phantasm_adapter = TypeAdapter(supported_from_phantasm_events)


def validate_from_phantasm(python_event, action_is_mandatory=True):
	try:
		event = from_phantasm_adapter.validate_python(python_event, context={"action_is_mandatory": action_is_mandatory})
	except ValidationError:
		event = None
	return event


def validate_from_phantasm_json(json_event, action_is_mandatory=True):
	try:
		event = from_phantasm_adapter.validate_json(json_event, context={"action_is_mandatory": action_is_mandatory})
	except ValidationError:
		event = None
	return event
