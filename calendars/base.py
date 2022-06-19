"""
Base Calendar
"""
from abc import ABC, abstractmethod
import logging
import traceback
from descriptions.languages import supported_languages


class BaseCalendar(ABC):
    """
    Base Calendar
    """
    name = 'base'

    def __init__(self, languages='en'):
        """

        """
        self.languages = self.validate_languages(languages)
        self.calender_description = None

    @staticmethod
    def validate_languages(languages):
        valid_languages = [lang for lang in languages.split(',') if lang in supported_languages]
        return valid_languages if valid_languages else ['en']

    def get_date_representation(self, **kwargs):
        """
        input: date datetime obj
        return: calendar representation
        """
        representation = {'day': kwargs['day'], 'month': [], 'year': kwargs['year'], 'weekday': []}
        for key, value in representation.items():
            for lang in self.languages:
                if key in ['month', 'weekday']:
                    try:
                        description = getattr(self.calender_description,
                                              f'{key.upper()}_{lang.upper()}')
                        representation[key] = description[kwargs[key]]
                    except KeyError:
                        logging.critical(traceback.format_exc())
                    except AttributeError:
                        logging.critical('%s is not supported', lang)
        return representation

    @abstractmethod
    def convert(self, date):
        """
        convert date to calendar system
        """

    @abstractmethod
    def convert_to_gregorian_date(self, year, month, day, timezone):
        """
        convert date to calendar system
        """

    def get_date(self, date):
        """
        get date calendar representation
        """
        year, month, day, weekday = self.convert(date)
        return self.get_date_representation(year=year, month=month, day=day, weekday=weekday)
