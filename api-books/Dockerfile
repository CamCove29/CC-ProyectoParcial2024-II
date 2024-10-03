FROM python:3-slim
WORKDIR /programas/api-books
RUN pip3 install flask
RUN pip install psycopg2
RUN pip install psycopg2-binary
COPY . .
RUN python3 db.py
CMD [ "python3", "./app.py" ]


