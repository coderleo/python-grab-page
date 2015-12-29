#coding=utf-8
import urllib2
import re
import json
class http_page(object):
	"""docstring for ClassName"""
	def __init__(self,base_url):
		super(http_page, self).__init__()
		#ww
		self.base_url = base_url

	def get_header(self):
		c = "SINAGLOBAL=1194854972418.3977.1438681067911; pf_feednav_bub_all_2074370833=1; myuid=2074370833; YF-Ugrow-G0=3a02f95fa8b3c9dc73c74bc9f2ca4fc6; login_sid_t=254015dcb4db1e614d9ddda26362b527; _s_tentry=passport.weibo.com; Apache=9978745845146.477.1451294569164; ULV=1451294569173:1:1:1:9978745845146.477.1451294569164:; YF-Page-G0=d0adfff33b42523753dc3806dc660aa7; SUS=SID-1898851205-1451294575-GZ-irzvt-b2af16e4f94b8f8f096484aa3bd46a3f; SUE=es%3Df864cc1bec8ccff8ae5cf39b0a4d278d%26ev%3Dv1%26es2%3D1d3c9460805eb7d3dd0085b5110db374%26rs0%3DzgLcJbgzmzF7vFeA3vjVX2GaxK0MmQ5cegXSzTnulRZQwSg5btLwPM02%252B8JW6MaDwyc8XKYphd3Acw6L4QE3fDcRvJEgh0u%252BE%252FGynkoG0mMXCGVF4qvBKpO3JR5BPLZ96cXWtcDEvugP%252FxvR%252BtE1fjJdJb2UQJWQJS%252FPcY6VOHA%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1451294575%26et%3D1451380975%26d%3Dc909%26i%3D6a3f%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D1898851205%26name%3Dleo.penguin%2540yahoo.com%26nick%3Dleo.penguin%26fmp%3D%26lcp%3D2015-10-23%252010%253A09%253A59; SUB=_2A257hI8_DeRxGedG4loZ9S_OyzmIHXVY8-f3rDV8PUNbuNBuLRTTkW8tpWJu0IEIR8fok-MPstqHxwCu9A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5lSECuBM_yuclJWvdfmaK25JpX5K2t; SUHB=0OMl5H8KePjjNJ; ALF=1482830574; SSOLoginState=1451294575; un=leo.penguin@yahoo.com; wvr=6; YF-V5-G0=8e216c747d9e492b2dcf025e8c7f492c; pf_feednav_bub_all_1898851205=1; pf_feednav_bub_hot_1898851205=1"
		self.request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')
		self.request.add_header('Host','weibo.com')
		self.request.add_header('Connection','keep-alive')
		self.request.add_header('Cookie',c)
	def get(self,id):	
		self.request = urllib2.Request(self.base_url+str(id))
		print self.base_url+str(id)
		self.get_header()	
		response = urllib2.urlopen(self.request)
		html = response.read()
		pattern = re.compile(r"<strong class=\\\"W_f1.\\\">.*?<\\\/strong>")
		match = pattern.findall(html)
		#pattern = re.compile(r'l') 
		#match = pattern.search('hello world!') 
		print match[1] 

		
