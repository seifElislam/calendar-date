"""
APP module
"""
from datetime import datetime
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import calendars

app = FastAPI()


@app.get("/")
async def today(lang='en'):
    date = datetime.today()
    response = {}
    for cls in calendars.order:
        calender = cls(lang)
        response.update({calender.name :calender.get_today_representation(date)})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
