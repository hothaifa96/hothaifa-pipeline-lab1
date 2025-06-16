FROM python:3.14.0b2-alpine3.22

WORKDIR /app

ENV WORKSPACE=$WORKDIR

RUN echo ${WORKSPACE} 

COPY  /movies-api/requirments.txt .

RUN pip3 install -r requirments.txt

COPY  /movies-api/movies.py .

EXPOSE 80

CMD ["python3","movies.py"]