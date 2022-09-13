# How to run
Before doing this, you need bot token.

If you don't have one, write to [@BotFather](https://t.me/BotFather) and get a new one.

After that, configure the environment variable `UDTW_TG_BOT_TOKEN`.

## Locally
```
pip install .
python3 -c "from udtw.tg.bot.application import run; run()"
```

## Using Docker
```
docker build -f .\.dockerfile .
docker run -it {received_docker_image_id}
```

### Example
```
$ docker run build -f .\.dockerfile .
...
=> => writing image sha256:52949ea9d6a343540f224d50a4c449f93167133d0828f8e087a68aea0d6faa47
...

$ docker run -it 52949ea9
```

# Environment variables
|Name|Type|Default|Description|
|-|-|-|-|
|`UDTW_TG_BOT_TOKEN`|`str`||Telegram bot token.|
|`UDTW_TG_BOT_TARGET_SPREADSHEET_ID`|`str`|`1DwfUKQ1jbBkMW-dPr1jRsYY-SifQDwUKqscXr67lCPk`|ID of checking spreadsheet.|
|`UDTW_TG_BOT_API_URL`|`str`|`http://localhost:5000`|`udtw-server` ip address.|

# Commands
|Name|Description
|-|-|
|`/check`|Displays a list of outdated orders.|
