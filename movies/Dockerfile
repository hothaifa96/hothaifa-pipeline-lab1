FROM python:3.14.0b2-alpine3.22

WORKDIR /app

ENV WORKSPACE=$WORKSPACE

COPY  requirments.txt .

RUN pip3 install -r requirments.txt

COPY  movies.py .

EXPOSE 80

CMD ["python3","movies.py"]