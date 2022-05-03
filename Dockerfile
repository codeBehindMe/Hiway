FROM python:3.9-buster

RUN mkdir app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8080" ]
