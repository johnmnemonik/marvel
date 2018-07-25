import asyncio
import aiohttp

from utils import func



characters, comics, events, creators, updates = [], [], [], [], []


async def search(res, name):
	data = res['data'].get('results')
	for page in data:
		if name == 'name':
			characters.append(page.get('name'))
			updates.append(page.get('modified').split('T1')[0])
		elif name == 'comics':
			comics.append(page.get('title'))
		elif name == 'events':
			events.append(page.get('description'))
		else:
			creators.append(page.get('firstName'))



async def crawler(url, name):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as res:
			resp = await res.json()
			await search(resp, name)



def main():
	obj = []
	flags = ['name', 'comics', 'events', 'creators']
	loop = asyncio.get_event_loop()
	result = func()
	task = [crawler(url, name) for url,name in zip(result, flags)]
	try:
		loop.run_until_complete(asyncio.gather(*task))
	except KeyboardInterrupt:
		pass
	finally:
		loop.close()

	for x in  zip(characters, comics, events, creators, updates):
		obj.append(x)
		print(x, end='\n\n\n')



if __name__ == '__main__':
	main()