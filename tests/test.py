import unittest

from listen.search import (
	netease_music_search,
	tencent_music_search,
	kugou_music_search,
	apple_music_search,
	qianqian_music_search,
)
	
class SearchFunctionTest(unittest.TestCase):
	def test_netease_music_search_happybrithdaytoyou(self):
		self.assertEqual(('祝你生日快乐', '群星') in netease_music_search('祝你生日快乐'), True)

	def test_netease_music_search_empty_string(self):
		self.assertEqual(netease_music_search(''), [])
			
	def test_tencent_music_search_happybrithdaytoyou(self):
		self.assertEqual(('祝你生日快乐', '儿歌') in tencent_music_search('祝你生日快乐'), True)

	def test_tencent_music_search_empty_string(self):
		self.assertEqual(tencent_music_search(''), [])
		
	def test_kugou_music_search_happybrithdaytoyou(self):
		self.assertEqual(('祝你生日快乐', '周杰伦') in kugou_music_search('祝你生日快乐'), True)
	
	def test_kugou_music_search_empty_string(self):
		self.assertEqual(kugou_music_search(''), [])
	
	def test_apple_music_search_happybrithdaytoyou(self):
		self.assertEqual(('祝你生日快乐', '小蓓蕾组合') in apple_music_search('祝你生日快乐'), True)
	
	def test_apple_music_search_empty_string(self):
		self.assertEqual(apple_music_search(''), [])
		
	def test_qianqian_music_search_happybrithdaytoyou(self):
		self.assertEqual(('祝你生日快乐', '白雪') in qianqian_music_search('祝你生日快乐'), True)
	
	def test_qianqian_music_search_empty_string(self):
		self.assertEqual(qianqian_music_search(''), [])
		
if __name__ == '__main__':
	unittest.main()