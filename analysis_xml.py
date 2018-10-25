#!/usr/bin/env python3    
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq

import bean_book

def analysisData(data):
	try:
		d = pq(data)
		body1 =d('body')
		s0 =body1('.hanghang-za-title').eq(0).text()
		body2 =body1('.hanghang-shu-content-font').text()
		s1 = body2.split('\n')
		n=0
		brif=''
		while n<s1.__len__():
			if n>2:
				brif=brif+s1[n]+'\n'
				pass
			n=n+1
			pass
		body3=body1('.hanghang-shu-content-btn')
		body4=body3('a').attr('href')
		b = bean_book.BookBean(s0, '',s1[0],s1[1],s1[2],brif,body4)
		return b
		pass
	except Exception as e:
		raise
	else:
		return bean_book.BookBean('','','','','','','')
		pass
	finally:
		pass
	pass


def analysisFile():
	with open('E:/data2', 'r',encoding='utf-8') as f:
		data = f.read()
		analysisData(data)
	pass

