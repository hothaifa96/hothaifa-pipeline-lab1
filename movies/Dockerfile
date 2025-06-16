FROM python:3.14.0b2-alpine3.22

WORKDIR /app

COPY  "/var/jenkins_home/workspace/hothiafas-pipeline/requirements.txt" .

RUN pip3 install -r requirements.txt

COPY "/var/jenkins_home/workspace/hothiafas-pipeline/movies.py" .

EXPOSE 80

CMD ["python3","movies.py"]