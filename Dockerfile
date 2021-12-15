#Dockerfile, image, container

FROM python:3.8
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
CMD [ "python", "./myapp.py" ]