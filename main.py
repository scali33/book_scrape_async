import aiohttp as ai
import asyncio
import requests
from pages.booksPage import BookPage

async def fecth(session,url):
    async with session.get(url) as res:
        return  await res.text()

async def get_all_pages(loop, urls):
    tasks = []
    async with ai.ClientSession(loop=loop) as seesion:
        for link in urls:
            tasks.append((fecth(seesion,link)))
        group_tasks = asyncio.gather(*tasks)
        return await group_tasks
main_loop = asyncio.get_event_loop()




page_content = requests.get(f'https://books.toscrape.com/catalogue/page-{1}.html').content
page = BookPage(page_content)
books = page.books

urls = [f'https://books.toscrape.com/catalogue/page-{c+1}.html'for c in range(1,page.page_count)]
res = main_loop.run_until_complete(get_all_pages(main_loop,urls))
for page_content in res:
    page = BookPage(page_content)
    books.extend(page.books)
