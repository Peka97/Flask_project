FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

RUN python flask init-db
RUN python flask create-users
RUN python flask create-artices
RUN python flask create-authos
RUN python flask create-tags

CMD ["python3", "wsgi.py"]
