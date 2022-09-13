# How to run

## Locally
```
pip install .
python3 -c "from udtw.server.application import run; run()"
```

## Using Docker
```
docker build -f .\.dockerfile .
docker run -p {wish_port}:5000 -it {received_docker_image_id}
```

### Example
```
$ docker run build -f .\.dockerfile .
...
=> => writing image sha256:52949ea9d6a343540f224d50a4c449f93167133d0828f8e087a68aea0d6faa47
...

$ docker run -p 404:5000 -it 52949ea9
...
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000    <-- in docker! it's 127.0.0.1:404 actually
 * Running on http://172.17.0.4:5000
...
```

# Environment variables
|Name|Type|Default|Description|
|-|-|-|-|
|`UDTW_SERVER_DEBUG`|`bool`|`True`||
|`UDTW_SERVER_HOST`|`str`|`0.0.0.0`||
|`UDTW_SERVER_PORT`|`int`|`5000`||
|`UDTW_SERVER_GOOGLE_CREDENTIALS_FILEPATH`|`str`|`<cwd>/credentials.json`|
|`UDTW_SERVER_DB_DATABASE`|`str \| None`|`None`|If not specified, the data is processed without writing to the database.|
|`UDTW_SERVER_DB_HOST`|`str`|`127.0.0.1`||
|`UDTW_SERVER_DB_PORT`|`int`|`5432`||
|`UDTW_SERVER_DB_USERNAME`|`str`|`postgres`||
|`UDTW_SERVER_DB_PASSWORD`|`str \| None`|`None`|Must be set if `UDTW_SERVER_DB_DATABASE` specified.|

# API Endpoints
|URL|Params|Response|Description|
|-|-|-|-|
|`/handle/spreadsheet/{spreadsheet_id}`||`Array of` [OrderInfo](#orderinfo)||

# Models

## OrderInfo
|Name|Type|Description|
|-|-|-|
|`id`|`int`||
|`order_id`|`int`||
|`cost_in_usd`|`float`||
|`delivery_at`|`date`||
|`cost_in_rub`|`float`||
