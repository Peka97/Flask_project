FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

RUN flask init-db
RUN flask create-users
RUN flask create-articles
RUN flask create-authors
RUN flask create-tags

CMD ["python3", "wsgi.py"]
