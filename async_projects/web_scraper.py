import asyncio, aiohttp
from bs4 import BeautifulSoup

urls = [
    "https://google.com",
    "https://youtube.com",
    "https://amazon.com",
]

async def req(session, url) -> None:
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        return await response.text()

async def scrape(url) -> None:
    async with aiohttp.ClientSession() as session:
         html = await req(session, url)
         soup = BeautifulSoup(html, 'html.parser')
         print(f"\n--- {url} ---\n{soup.title.string.strip() if soup.title else 'N/A'}\n")

async def main() -> None:
        await asyncio.gather(*(scrape(url) for url in urls))
            


if __name__ == '__main__':
    asyncio.run(main())
