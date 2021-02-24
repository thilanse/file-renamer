FROM python:3.6-slim
WORKDIR /app
RUN mkdir test
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
ENTRYPOINT python testing-docker.py