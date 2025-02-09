FROM python:latest

WORKDIR /flask-app 

COPY . . 

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]

EXPOSE 5000
