"""
Gregorian calendar
"""
import convertdate
from calendars.base import BaseCalendar
import descriptions.hijri as hijri_representation


class Hijri(BaseCalendar):
    """
    Hijri Calendar
    """
    name = 'hijri'

    def __init__(self, languages):
        """
        Init calendar with Gregorian representation
        """
        super().__init__(languages)
        self.calender_description = hijri_representation

    def convert(self, date):
        """
        convert date to Hijri system
        """
        year, month, day = convertdate.islamic.from_gregorian(date.year, date.month, date.day+1)
        return year, month, day, date.weekday()
