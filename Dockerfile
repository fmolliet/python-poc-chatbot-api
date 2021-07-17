FROM python:3.7.8-slim

RUN pip install --no-cache-dir spacy chatterbot_corpus flask requests chatterbot
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en

ENV APP_HOME /app
WORKDIR $APP_HOME


COPY . . 

EXPOSE $PORT
ENTRYPOINT ["python src/app.py"]