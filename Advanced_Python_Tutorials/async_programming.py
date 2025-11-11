import asyncio
import random


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay

    data = {"data": "Sample data"}
    print("Data fetched.")

    return data


async def process_data(data):
    print("Processing data...")
    await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate processing delay

    print("processed data: ", {data["data"]})
 