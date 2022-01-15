"""
Base Calendar
"""
from abc import ABC, abstractmethod
import logging
import traceback
import convertdate


class BaseCalendar(ABC):
    """

    """
    name = 'base'

    def __init__(self, languages='en'):
        """

        """
        self.languages = languages.split(',')
        self.calender_description = None

    def get_date_representation(self, date):
        """
        input: date datetime obj
        return: calendar representation
        """
        representation = {'day': date.day, 'month': [], 'year': date.year, 'weekday': []}
        for key, value in representation.items():
            for lang in self.languages:
                if isinstance(value, list):
                    try:
                        description = getattr(self.calender_description, f'{key.upper()}_{lang.upper()}')
                        code = getattr(date, key)() if key == 'weekday' else getattr(date, key)
                        value.append({lang: description[code]})
                    except KeyError:
                        logging.critical(traceback.format_exc())
        return representation
    
    @abstractmethod
    def convert(self, date):
        """
        convert date to calendar system
        """
        
    def get_date(self, date):
        """
        get date calendar representation
        """
        converted_date = self.convert(date)
        return self.get_date_representation(converted_date)