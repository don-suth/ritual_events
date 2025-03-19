from datetime import datetime
from pydantic import BaseModel


class AuthenticateData(BaseModel):
	token: str = "Hello!"


class AuthenticateAction(BaseModel):
	time: datetime
	action: str = "Authenticate"
	data: AuthenticateData


class OpenDoorAction(BaseModel):
	time: datetime
	action: str = "OpenDoor"


class CloseDoorAction(BaseModel):
	time: datetime
	action: str = "CloseDoor"
