"""

"""
import pytz
from pydantic import BaseModel, Field, validator
from calendars import order
from descriptions.languages import supported_languages


def validate_timezone(requested_timezone):
    """
    Validate requested timezone
    """
    if requested_timezone not in pytz.all_timezones_set:
        return 'Africa/Cairo'
    return requested_timezone


class FindRequestBody(BaseModel):
    calendar: str
    day: int = Field(gt=0, lt=31, description="31 >= day >= 1")
    month: int = Field(gt=0, lt=13, description="12 >= month >= 1")
    year: int = Field(gt=1400, lt=3000)
    language: str = 'en'
    timezone: str = 'Africa/Cairo'

    @validator('calendar')
    def validate_calendar_name(cls, calendar_name):
        if calendar_name.lower() not in [c.name for c in order]:
            raise ValueError('Invalid calendar name')
        return calendar_name.lower()

    @validator('language')
    def validate_language(cls, language):
        if language.lower() not in supported_languages:
            raise ValueError('Invalid language')
        return language.lower()

    @validator('timezone')
    def validate_timezone(cls, timezone):
        return validate_timezone(timezone)
