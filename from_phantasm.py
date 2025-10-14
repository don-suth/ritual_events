from base_event import BaseEvent
from typing import Literal


class AuthenticateEvent(BaseEvent):
	action: Literal["Authenticate"] = "Authenticate"
	token: str

class OpenDoorAction(BaseEvent):
	action: Literal["OpenDoor"] = "OpenDoor"

class CloseDoorAction(BaseEvent):
	action: Literal["CloseDoor"] = "CloseDoor"
