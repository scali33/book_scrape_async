import aiohttp as ai
import asyncio
import time

async def fetch_page(seesion,url):
    page_start = time.time()
    async with seesion.get(url) as res:
        print(f'page took {time.time() - page_start} ')
        return res.status
async def get_muti_page(loop, *urls):
    task = []
    async with ai.ClientSession(loop=loop) as seesion:
        for url in urls:
            task.append(fetch_page(seesion,url))
        group_tasks = asyncio.gather(*task)
        return await group_tasks 
        
loop = asyncio.get_event_loop()

urls = ['http://google.com' for _ in range(50)]
start = time.time()
loop.run_until_complete(get_muti_page(loop,*urls))
print('took',time.time()-start)
