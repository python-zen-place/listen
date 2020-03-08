import json
import re
import requests
		
def require_keyword(func):
	def wapper(*args, **kwargs):
		if not args[0]:
			return []
		else:
			return func(*args, **kwargs)
	return wapper

def assert_no_keyerror(func):
	def wapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except KeyError as e:
			return []
			print(f'{func.__name__} : KeyError')
	return wapper

def assert_no_indexerror(func):
	def wapper(*args, **kwargs):
		try:
		 	return func(*args, **kwargs)
		except IndexError as e:
		 	print(f'{func.__name__}: IndexError')
		 	return []
	return wapper

@assert_no_keyerror		 	
@require_keyword
def netease_music_search(keyword):
	url = f'https://music.jeeas.cn/v1/search?s={keyword}&from=music'
	songs = requests.get(url).json()['result']['songs']
	return [(song['name'], song['ar'][0]['name']) for song in songs if keyword in song['name']]

@assert_no_keyerror		 	
@require_keyword		
def tencent_music_search(keyword):
	url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?w={keyword}'
	songs = json.loads(requests.get(url).text.strip('callback')[1:-1])['data']['song']['list']
	return [(song['songname'], song['singer'][0]['name']) for song in songs if keyword in song['songname']]

@assert_no_keyerror		 	
@require_keyword
def kugou_music_search(keyword):
	url = f'https://songsearch.kugou.com/song_search_v2?keyword={keyword}'
	songs = requests.get(url).json()['data']['lists']
	return [(song['SongName'], song['SingerName']) for song in songs if keyword in song['SongName']]

@assert_no_indexerror
@assert_no_keyerror		 	
@require_keyword
def apple_music_search(keyword):
	url = f'http://tools.applemusic.com/zh-cn/search?country=cn&media=songs&utf8=%E2%9C%93&term={keyword}&country=cn&media=songs&cache='
	headers = {
		'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
		'Connection': 'keep-alive',
		'Host': 'tools.applemusic.com',
		'Referer': 'http://tools.applemusic.com/zh-cn?country=cn&media=songs&term=%E5%A4%8D%E5%91%98',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
		'X-CSRF-Token': '8jxc7JXEgefdr17j7WpY0HRexX3cZ6FZXpFGObYxETt/DDJOIQgW3mga0k9R8ohLwbpIuoBEQBZ2bjYd74Ez7Q==',
		'X-NewRelic-ID': 'VQIHUl9RDxACXFBaDgABVQ==',
		'X-Requested-With': 'XMLHttpRequest'
	}
	songs = json.loads('{"items":'+re.findall('append\(itemsTemplate\((.*)', requests.get(url, headers=headers).text)[0][7:-3])['items']
	return [(song['name'], song['artistOrCuratorName']) for song in songs if keyword in song['name']]

@assert_no_keyerror
@require_keyword
def qianqian_music_search(keyword):
	url = f'https://sug.qianqian.com/info/suggestion?format=json&word={keyword}'
	songs = requests.get(url).json()['data']['song']
	return [(song['songname'], song['artistname']) for song in songs if keyword in song['songname']]