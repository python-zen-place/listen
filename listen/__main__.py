import getopt
import sys
from listen.search import (
	netease_music_search,
	tencent_music_search,
	kugou_music_search,
	apple_music_search,
	qianqian_music_search,
)

from listen.utils import formatter, filter

help_content = '''listen
Usage:
  python -m listen <song-name> [-a <artist-name>] [-w]
  python -m listen listen -h
Options:
  -h --help         Show this screen.
  -a <artist-name>  Search song of specific artist
  -w                Exact search mode
'''

try:
	opts, args = getopt.gnu_getopt(sys.argv[1:], 'hwa:', ['help'])
	for opt, value in opts:
		if opt in ('-h', '--help'):
			print(help_content)
			sys.exit()
		print(sys.getrefcount(value))
	keyword = ' '.join(args)
	print(keyword)
	results = {
		'网易云音乐': netease_music_search(keyword),
		'QQ音乐': tencent_music_search(keyword),
		'酷狗音乐':  kugou_music_search(keyword),
		'Apple Music': apple_music_search(keyword),
		'千千音乐': qianqian_music_search(keyword),
	}

	for opt, value in opts:
		if opt in ('-w',):
			for platform, songs in results.items():
				results[platform] = filter.filter_blur_search(songs, keyword)
		if opt in ('-a',):
			for platform, songs in results.items():
				results[platform] = filter.filter_artist(songs, value)
	for platform, songs in results.items():
		formatter.prettify_output(platform, songs)

except getopt.GetoptError as e:
	print(help_content)
	print(f'listen: error: {e}')