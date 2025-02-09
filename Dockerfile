FROM python:3.12-alpine

WORKDIR /flask-app 

RUN mkdir static
COPY static ./static/.

COPY app.py requirements.txt .

RUN pip install -r requirements.txt


ENTRYPOINT ["python3"]
CMD ["app.py"]

EXPOSE 5000
