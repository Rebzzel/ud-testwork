FROM python:3.10
WORKDIR /app
COPY . .

RUN pip install .

ENV UDTW_TG_BOT_API_URL=http://host.docker.internal:5000

ENTRYPOINT [ "python3", "-c", "from udtw.tg.bot.application import run; run()" ]
