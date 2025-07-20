import aiohttp, asyncio

# https://developers.coindesk.com/documentation/data-api/index_cc_v1_latest_tick

async def poll() -> None:
    async with aiohttp.ClientSession() as session:
        for _ in range(5):
            async with session.get("https://data-api.coindesk.com/index/cc/v1/latest/tick/market=cadli&instruments=BTC-USD,ETH-USD&apply_mapping=true") as response:
                data = await response.json()
                print(f"BTC Price: {data["Data"]["BTC-USD"]["VALUE"]}")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(poll())