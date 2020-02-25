import unittest

from listen.search import (
	netease_music_search,
	tencent_music_search,
	kugou_music_search,
	apple_music_search,
)
	
class SearchFunctionTest(unittest.TestCase):
	def test_netease_music_search_happybrithdaytoyou(self):
		self.assertCountEqual(netease_music_search('祝你生日快乐'), [('祝你生日快乐', '小蓓蕾组合'), ('祝你生日快乐', '宝宝巴士'), ('祝你生日快乐', '马英伦'), ('祝你生日快乐', '云雀合唱团'), ('祝你生日快乐', '胡彦斌'), 
																   ('祝你生日快乐', '马忠宇'), ('祝你生日快乐', 'Neko猫桑'), ('祝你生日快乐', '徐泽'), ('祝你生日快乐', '群星'), ('祝你生日快乐', '周晓畅')])
	def test_netease_music_search_empty_string(self):
		with self.assertRaises(KeyError):
			netease_music_search('')
			
	def test_tencent_music_search_happybrithdaytoyou(self):
		self.assertCountEqual(tencent_music_search('祝你生日快乐'), [('祝你生日快乐', '儿歌'), ('祝你生日快乐', '范晓萱'), ('祝你生日快乐', '宝宝巴士儿歌'), ('祝你生日快乐', '雷佳'), ('祝你生日快乐', '小蓓蕾组合'), 
																   ('祝你生日快乐', '红蔷薇'), ('祝你生日快乐', '韩磊')])

	def test_tencent_music_search_empty_string(self):
		self.assertEqual(tencent_music_search(''), [])
		
	def test_kugou_music_search_happybrithdaytoyou(self):
		self.assertCountEqual(kugou_music_search('祝你生日快乐'), [('祝你生日快乐', '儿童歌曲'), ('祝你生日快乐', '宝宝巴士'), ('祝你生日快乐', '纯音乐'), ('祝你生日快乐', '韩磊'), ('祝你生日快乐', '云雀合唱团'), 
												  ('祝你生日快乐', '周杰伦'), ('祝你生日快乐', '雷佳、王俊凯'), ('祝你生日快乐', '胡彦斌'), ('祝你生日快乐', '叶晓红'), ('祝你生日快乐', '兔小贝'), 
												  ('祝你生日快乐', '雷佳'), ('祝你生日快乐', '陈永强'), ('祝你生日快乐', '司文'), ('祝你生日快乐', '彭野')])

	def test_kugou_music_search_empty_string(self):
		self.assertListEqual(kugou_music_search(''), [])
	
	def test_apple_music_search_happybrithdaytoyou(self):
		self.assertCountEqual(apple_music_search('祝你生日快乐'), [('祝你生日快乐', '小蓓蕾组合'), ('祝你生日快乐', '小蓓蕾组合'), ('祝你生日快乐', '杨烁'), ('祝你生日快乐', '小蓓蕾组合'), ('祝你生日快乐', '小蓓蕾组合')])
	
	def test_apple_music_search(self):
		self.assertListEqual(apple_music_search(''), [])
		
if __name__ == '__main__':
	unittest.main()