from datetime import datetime
from pydantic_extra_types.color import Color as Colour
from typing import Literal
from base_event import BaseEvent

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
