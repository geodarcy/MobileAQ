# import packages
import asyncio
from airgradient import AirGradientClient
import dataclasses
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
import json

# set up writing to InfluxDB
load_dotenv()
token = os.getenv("INFLUXDB_TOKEN")
org = "geopi"
url = "http://localhost:8086"
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket = "mobilegeo"
write_api = write_client.write_api(write_options=SYNCHRONOUS)


async def main() -> None:
    async with AirGradientClient('10.42.0.155') as client:
        measurements = await client.get_current_measures()
        p = influxdb_client.Point('aq_measurement') \
            .from_dict({'measurement': 'test',
                        'tags': {'home': 'aq'},
                        'fields': dataclasses.asdict(measurements)})
        write_api.write(bucket=bucket, record=p)


if __name__ == "__main__":
    asyncio.run(main())
