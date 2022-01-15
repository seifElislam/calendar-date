"""
Base Calendar
"""
from abc import ABC, abstractmethod
import convertdate


class BaseCalendar(ABC):
    """

    """
    name = 'base'

    def __init__(self, languages='en'):
        """

        """
        self.languages = languages.split(',')

    @abstractmethod
    def get_today_representation(self, today):
        """
        input: today datetime obj
        return: calendar representation
        """
