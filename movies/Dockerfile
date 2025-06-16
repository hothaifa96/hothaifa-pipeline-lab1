FROM python:3.14.0b2-alpine3.22

WORKDIR /app

ENV WORKSPACE=$WORKSPACE

RUN echo ${WORKSPACE} 

COPY  ${WORKSPACE}/movies-api/requirments.txt .

RUN pip3 install -r requirments.txt

COPY  ${WORKSPACE}/movies-api/movies.py .

EXPOSE 80

CMD ["python3","movies.py"]