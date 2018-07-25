from hashlib import md5
from random import randint


def build_md5(url):
	publik_key  = 'ffa0bb02c7ece0999803af25210e8b9c'
	private_key = 'c6c3d24659cdf5b0dcd9d17e4ec854eac63c847f'
	ts = str(randint(1, 100))
	dgst = ts + private_key + publik_key
	hs = md5(dgst.encode('utf-8')).hexdigest()
	return url.format(ts, publik_key, hs)


def func():
	urls = [
		"http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}",
		"http://gateway.marvel.com/v1/public/comics?ts={}&apikey={}&hash={}",
		"http://gateway.marvel.com/v1/public/events?ts={}&apikey={}&hash={}",
		"http://gateway.marvel.com/v1/public/creators?ts={}&apikey={}&hash={}"
	]

	return [build_md5(url) for url in urls]