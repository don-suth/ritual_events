from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from pydantic_extra_types.color import Color as Colour


class EntranceEnum(str, Enum):
	TAV = "Tav"
	GUILD = "Guild"


class LetMeInData(BaseModel):
	name: str
	entrance: EntranceEnum


class LetMeInAction(BaseModel):
	time: datetime
	action: str = "LetMeIn"
	data: LetMeInData


class FoodRunData(BaseModel):
	arrival_time: datetime
	entrance: EntranceEnum


class FoodRunAction(BaseModel):
	time: datetime
	action: str = "FoodRun"
	data: FoodRunData


class ClockSettingsUpdateData(BaseModel):
	brightness: int | None
	text_colour: Colour | None
	alternate_seconds_indicator: bool | None


class ClockSettingsUpdateAction(BaseModel):
	time: datetime
	action: str = "ClockSettingsUpdate"
	data: ClockSettingsUpdateData
