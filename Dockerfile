FROM python:3.8-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT python main.py
