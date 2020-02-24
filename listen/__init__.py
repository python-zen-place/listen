import json
import re
import requests


def search(keyword):
 	pass
		
def netease_music_search(keyword):
	url = f'https://music.jeeas.cn/v1/search?s={keyword}&from=music'
	songs = requests.get(url).json()['result']['songs']
	return [(song['name'], song['ar'][0]['name']) for song in songs if song['name'] == keyword]

def tencent_music_search(keyword):
	url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?w={keyword}'
	songs = json.loads(requests.get(url).text.strip('callback')[1:-1])['data']['song']['list']
	return [(song['songname'], song['singer'][0]['name']) for song in songs if song['songname'] == keyword]

def kugou_music_search(keyword):
	url = f'https://songsearch.kugou.com/song_search_v2?keyword={keyword}'
	songs = requests.get(url).json()['data']['lists']
	return [(song['SongName'], song['SingerName']) for song in songs if song['SongName'] == keyword]

def apple_music_search(keyword):
	url = f'http://tools.applemusic.com/zh-cn/search?country=cn&media=songs&utf8=%E2%9C%93&term={keyword}&country=cn&media=songs&cache=&_=1582535609057'
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
	data = re.findall('append\(itemsTemplate\((.*)', requests.get(url, headers=headers).text)[0][:-3]
	return data

if __name__ == '__main__':
	pass
