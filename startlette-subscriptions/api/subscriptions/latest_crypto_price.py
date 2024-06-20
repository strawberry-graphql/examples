from typing import AsyncGenerator
import json
from datetime import datetime

import strawberry
import websockets


@strawberry.type
class Ticker:
    pair: str
    best_ask_price: str
    best_bid_price: str
    close_price: str
    timestamp: datetime


@strawberry.subscription
async def latest_crypto_price(pair: str = "ETH/EUR") -> AsyncGenerator[Ticker, None]:
    async with websockets.connect("wss://ws.kraken.com") as websocket:
        await websocket.send(
            json.dumps(
                {
                    "event": "subscribe",
                    "pair": [pair],
                    "subscription": {"name": "ticker"},
                }
            )
        )

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            if "event" in data:
                if "status" in data and data["status"] == "error":
                    raise Exception(data["errorMessage"])

            if isinstance(data, list):
                yield Ticker(
                    pair=pair,
                    best_ask_price=data[1]["a"][0],
                    best_bid_price=data[1]["b"][0],
                    close_price=data[1]["c"][0],
                    timestamp=datetime.now(),
                )
