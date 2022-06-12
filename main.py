"""
APP module
"""
from datetime import datetime
import json
from random import randint
import pytz
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import calendars

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


with open('quotes/wiki_quotes.json') as f:
    quotes = json.load(f)


def validate_timezone(requested_timezone):
    """
    Validate requested timezone
    """
    if requested_timezone not in pytz.all_timezones_set:
        return 'Africa/Cairo'
    return requested_timezone


def get_calendars_by_gregorian(gregorian_date, lang):
    """
    Get date in available calendars by gregorian date
    """
    response = {}
    for cls in calendars.order:
        calender = cls(lang)
        response.update({calender.name: calender.get_date(gregorian_date)})
    return response


@app.get("/")
async def today(lang='en', timezone='Africa/Cairo'):
    # validate timezone
    valid_timezone = validate_timezone(timezone)
    date = datetime.now(tz=pytz.timezone(valid_timezone))

    response = get_calendars_by_gregorian(date, lang)
    response.update({'quote': quotes[randint(0, len(quotes)-1)]})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
