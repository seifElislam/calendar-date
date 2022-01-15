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

    def get_today_representation(self, today):
        """
        input: today datetime object
        return: Gregorian calendar representation
        """
        representation = {'day': today.day, 'month': [], 'year': today.year, 'weekday': []}
        for key, value in representation.items():
            for lang in self.languages:
                if isinstance(value, list):
                    try:
                        description = getattr(gre_representation, f'{key.upper()}_{lang.upper()}')
                        code = getattr(today, key)() if key == 'weekday' else getattr(today, key)
                        value.append({lang: description[code]})
                    except KeyError:
                        logging.critical(traceback.format_exc())
        return representation
