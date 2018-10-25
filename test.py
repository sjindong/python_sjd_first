#!/usr/bin/env python3    
# -*- coding: utf-8 -*-
import random,time
import os

import sendmail
import db_book_sqlite  as DB
import config
import requets_x
import analysis_xml
def once(cursor,num,t):
	num_book = str(num)
	url=config.getUrl(num_book)
	data = requets_x.reX( url)
	book = analysis_xml.analysisData(data)
	book.set_bookID(num_book)
	print(num_book +" is ok   | name = "+book.get_name())
	DB.addBook(cursor,book)
	if book.get_url() == "":
		t = t+1
		pass
	else:
		t=0
		pass
	return  t
	pass

def delayTime_Random():
	time.sleep(random.uniform(0,1.5))
	pass

def autoGet(cursor,f,num_book_init):
	t=0
	num_book=num_book_init
	while num_book<20000 or t<30:
		num_book = num_book +1
		t=once(cursor,num_book,t)
		set(f,num_book)
		delayTime_Random()
		pass

	sendmail.sendEmail('raspberry  stop',"work is stop \n  and  the last num is  ： "+str(num_book))
	pass

def get(f):
	return f.read()
	pass

def set(f,num):
	f.seek(0)
	f.truncate()
	f.write(str(num))
	f.flush()
	pass

def init_file(file):
	if os.path.exists(file):
	    with open(file,mode='r',encoding='utf-8') as ff:
	        num = ff.read()
	        if  not num:
	        	num='0'
	        pass
	else:
	    with open(file, mode='a', encoding='utf-8') as ff:
	    	num ='0'
	    pass
	return num
	pass

if __name__ == '__main__':
	print("create db")
	cursor = DB.getCursor(config.db_path)
	print("create table")
	DB.initDB(cursor)

	num = init_file(config.Down_Num)
	# print(num)

	with open(config.Down_Num, 'w+',encoding='utf-8') as f:
		autoGet(cursor,f,int(num))
	pass

	# aa = DB.selectBookID(cursor)
	# once(15,0)
