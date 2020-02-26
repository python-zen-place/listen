from typing import List, Tuple

def prettify_output(platfrom: str, songs: List[Tuple[str, str]]):
	print(f'{platfrom}:')
	if len(songs) == 0:
		print('暂无版权')
	for song in songs:
		song_name, singer_name = song
		print(f'{song_name}-{singer_name}')
	print('------------------------------------------------------------------')
