import sys

from listen.search import (
	netease_music_search,
	tencent_music_search,
	kugou_music_search,
	apple_music_search
)

from listen.utils import formatter

try:
	keyword = sys.argv[1]
	formatter.prettify_output('网易云音乐', netease_music_search(keyword))
	formatter.prettify_output('QQ音乐', tencent_music_search(keyword))
	formatter.prettify_output('酷狗音乐', kugou_music_search(keyword))
	formatter.prettify_output('Apple Music', apple_music_search(keyword))
except IndexError as e:
	print('usage: listen SONG_NAME')
	print('listen: error: the following arguments are required: SONG_NAME')