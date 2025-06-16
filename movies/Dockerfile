FROM python:3.14.0b2-alpine3.22

WORKDIR /app

COPY  ../movies-api/requirements.txt .

RUN pip3 install -r requirements.txt

COPY  ../movies-api//movies.py .

EXPOSE 80

CMD ["python3","movies.py"]