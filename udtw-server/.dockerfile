FROM python:3.10
WORKDIR /app
COPY . .

RUN pip install .

ENV UDTW_SERVER_HOST=0.0.0.0
ENV UDTW_SERVER_PORT=5000
ENV UDTW_SERVER_DEBUG=False

ENTRYPOINT [ "python3", "-c", "from udtw.server.application import run; run()"]
