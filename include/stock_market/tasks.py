from airflow.hooks.base import BaseHook
import  json
from io import BytesIO
from minio import Minio
from airflow.exceptions import AirflowNotFoundException

BUCKET_NAME = 'stock-market'

def _get_minio_clent():
    minio = BaseHook.get_connection('minio')
    client = Minio(
        endpoint=minio.extra_dejson['endpoint_url'].split('//')[1],
        access_key=minio.login,
        secret_key=minio.password, 
        secure=False
    )
    return client
# These are the tasks executed by the DAG - stock_market.py

# Gets Stock Prices and outputs the data as JSON
def _get_stock_prices(url, symbol):
    import requests
    import json

    url = f"{url}{symbol}?metrics=high?&interval=1d&range=1y"
    api = BaseHook.get_connection('stock_api')
    response = requests.get(url, headers=api.extra_dejson['headers'])
    return json.dumps(response.json()['chart']['result'][0])

# Store Prices Function returns the path to the stored object in the format required in the MinIO Storage
def _store_prices(stock):
    client = _get_minio_clent()
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
    stock = json.loads(stock)
    symbol = stock['meta']['symbol']
    data = json.dumps(stock, ensure_ascii=False).encode('utf8')
    obgw = client.put_object(
        bucket_name = BUCKET_NAME, 
        object_name = f'{symbol}/prices.json',
        data = BytesIO(data),
        length = len(data)
        )
    return f'{obgw.bucket_name}/{symbol}'

def _get_formatted_csv(path):
    client = _get_minio_clent()
    prefix_name = f"{path.split('/')[1]}/formatted_prices/"
    objects = client.list_objects(BUCKET_NAME, prefix=prefix_name, recursive = True)
    for obj in objects:
        if obj.object_name.endswith('.csv'):
            return obj.object_name
    return AirflowNotFoundException(f'No CSV file found')