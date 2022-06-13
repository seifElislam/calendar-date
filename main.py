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
from utils import FindRequestBody, validate_timezone
from descriptions.languages import supported_languages

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
    response.update({'quote': quotes[randint(0, len(quotes) - 1)]})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/jump/")
async def jump_to_date(request_body: FindRequestBody):
    calendar_class = [cls for cls in calendars.order if cls.name == request_body.calendar][0]
    requested_date = calendar_class(request_body.language).convert_to_gregorian_date(
        request_body.year, request_body.month, request_body.day, request_body.timezone)
    response = get_calendars_by_gregorian(requested_date, request_body.language)
    response.update({'quote': quotes[randint(0, len(quotes) - 1)]})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.get('/calendars/')
async def get_supported_calendars(lang='en'):
    """

    """
    supported_calenders = {
        cls(lang).name: getattr(cls(lang).calender_description, 'NAME_{}'.format(lang.upper()))
        for cls in calendars.order}
    return JSONResponse(status_code=200, content={'calendars': supported_calenders})


@app.get('/calendars/{calendar_name}/months')
async def get_calendar_month_description(calendar_name, lang='en'):
    """

    """
    # validate languages
    if lang not in supported_languages:
        return JSONResponse(status_code=400, content={"error": "Not supported language"})
    requested_calendars = [cls for cls in calendars.order if cls.name == calendar_name]
    if not requested_calendars:
        return JSONResponse(status_code=400, content={"error": "Invalid calendar"})
    calendar_obj = requested_calendars[0](lang)
    return JSONResponse(status_code=200, content={
        'months': getattr(calendar_obj.calender_description, 'MONTH_{}'.format(lang.upper()))})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
