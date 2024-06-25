FROM python:3

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN export FLASK_APP=app

RUN export FLASK_ENV=development

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]