#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def reX(url):
	r = requests.get(url)
	r.encoding = 'utf-8'
	print (r.status_code)
	data = r.text
	return data
	pass