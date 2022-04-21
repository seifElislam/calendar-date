"""
APP module
"""
from datetime import datetime, timezone
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


with open('quotes/wiki_quotes.json', encoding='utf8') as f:
    quotes = json.load(f)


@app.get("/")
async def today(lang='en'):
    date = datetime.now(tz=pytz.timezone('Africa/Cairo'))
    response = {}
    for cls in calendars.order:
        calender = cls(lang)
        response.update({calender.name: calender.get_date(date)})
    response.update({'quote': quotes[randint(0, len(quotes)-1)]})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
