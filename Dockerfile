FROM python:3.8.2-slim-buster

  
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]