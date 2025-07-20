import asyncio, aiohttp

# https://www.fisheries.noaa.gov/foss/f?p=215:35:4376356816298:::::

urls = [
     "https://apps-st.fisheries.noaa.gov/ods/foss/landings/",
     "https://apps-st.fisheries.noaa.gov/ods/foss/trade_data/",
     "https://apps-st.fisheries.noaa.gov/ods/foss/vessel_data/"
]

async def get_data(session, url):
    data = []
    offset = 0
    limit = 1000
    while True:
        async with session.get(f'{url}?offset={offset}&limit={limit}') as response:
            json_resp = await response.json()
            data.extend(json_resp.get("items", []))
            if json_resp["hasMore"] == "false":
                break
            offset += limit
    print(data)

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(get_data(session, url) for url in urls))

if __name__ == '__main__':
    asyncio.run(main())