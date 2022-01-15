"""
APP module
"""
from datetime import datetime
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    today = datetime.today()
    content = {"today": f'{today.strftime("%A, %d. %B %Y %I:%M%p")}'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
