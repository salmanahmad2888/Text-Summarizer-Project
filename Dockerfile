FROM python:3.11.4-alpine

RUN apk update  && apk add --no-cache aws-cli
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip instaclsll transformers accelerate

CMD ["python3", "app.py"]