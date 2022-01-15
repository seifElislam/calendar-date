"""
Gregorian calendar
"""
import logging
import traceback
from calendars.base import BaseCalendar
import descriptions.gregorian as gre_representation


class Gregorian(BaseCalendar):
    """

    """
    name = 'gregorian'

    def __init__(self, languages):
        """

        """
        super().__init__(languages)
        self.calender_description = gre_representation

    def convert(self, date):
        """

        """
        return date
