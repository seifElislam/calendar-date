"""
Base Calendar
"""
from abc import ABC, abstractmethod
import logging
import traceback


class BaseCalendar(ABC):
    """

    """
    name = 'base'

    def __init__(self, languages='en'):
        """

        """
        self.languages = languages.split(',')
        self.calender_description = None

    def get_date_representation(self, **kwargs):
        """
        input: date datetime obj
        return: calendar representation
        """
        representation = {'day': kwargs['day'], 'month': [], 'year': kwargs['year'], 'weekday': []}
        for key, value in representation.items():
            for lang in self.languages:
                if isinstance(value, list):
                    try:
                        description = getattr(self.calender_description,
                                              f'{key.upper()}_{lang.upper()}')
                        value.append({lang: description[kwargs[key]]})
                    except KeyError:
                        logging.critical(traceback.format_exc())
                    except AttributeError:
                        logging.critical(f'{lang} is not supported')
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
        year, month, day, weekday = self.convert(date)
        return self.get_date_representation(year=year, month=month, day=day, weekday=weekday)
