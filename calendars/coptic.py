"""
Coptic calendar
"""
import pytz
from datetime import datetime
import convertdate
from calendars.base import BaseCalendar
import descriptions.coptic as coptic_representation


class Coptic(BaseCalendar):
    """
    Coptic Calendar
    """
    name = 'coptic'

    def __init__(self, languages):
        """
        Init calendar with Coptic representation
        """
        super().__init__(languages)
        self.calender_description = coptic_representation

    def convert(self, date):
        """
        convert date to Coptic system
        """
        year, month, day = convertdate.coptic.from_gregorian(date.year, date.month, date.day)
        return year, month, day, date.weekday()

    def convert_to_gregorian_date(self, year, month, day, timezone):
        """

        """
        return pytz.timezone(timezone).localize(datetime(*convertdate.coptic.to_gregorian(year, month, day)))
