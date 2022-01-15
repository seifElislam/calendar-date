"""
Gregorian calendar
"""
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
