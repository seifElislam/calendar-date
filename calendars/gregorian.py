"""
Gregorian calendar
"""
import pytz
from datetime import datetime
from calendars.base import BaseCalendar
import descriptions.gregorian as gre_representation


class Gregorian(BaseCalendar):
    """
    Gregorian Calendar
    """
    name = 'gregorian'

    def __init__(self, languages):
        """
        Init calendar with Gregorian representation
        """
        super().__init__(languages)
        self.calender_description = gre_representation

    def convert(self, date):
        """
        convert date to Gregorian system
        """
        return date.year, date.month, date.day, date.weekday()

    def convert_to_gregorian_date(self, year, month, day, timezone):
        """

        """
        return pytz.timezone(timezone).localize(
            datetime(year=year, month=month, day=day, tzinfo=timezone))
