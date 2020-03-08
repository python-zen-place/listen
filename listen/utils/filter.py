from typing import List, Tuple

# song[0] is song name 
# song[1] is artist name

def filter_blur_search(songs: List[Tuple[str, str]], keyword: str) -> List[Tuple[str, str]]:
	return [song for song in songs if song[0] == keyword]

def filter_artist(songs: List[Tuple[str, str]], artist: str) -> List[Tuple[str, str]]:
	return [song for song in songs if song[1] == artist]

