FROM python:3.7.3

WORKDIR /dockerapp

COPY ./requirements.txt /dockerapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dockerapp/requirements.txt

COPY ./api /dockerapp/api

CMD ["python", "api.py"]