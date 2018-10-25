#!/usr/bin/env python3   
# -*- coding: utf-8 -*-

import sqlite3

import bean_book as BeanBook
import config

def getCursor(db_path):
	conn=sqlite3.connect(db_path)
	conn.text_factory=str
	cursor = conn.cursor()
	return conn

def initDB(cursor):
	cursor.execute('create table IF NOT EXISTS book ( id INTEGER PRIMARY KEY AUTOINCREMENT, '+ #
		BeanBook.Book.name.value+' varchar(200),'+
		BeanBook.Book.bookID.value+' varchar(40),'+
		BeanBook.Book.author.value+' varchar(40),'+
		BeanBook.Book.bookType.value+' varchar(40),'+
		BeanBook.Book.point.value+' varchar(20),'+
		BeanBook.Book.briefIntro.value+' varchar(1000),'+
		BeanBook.Book.url.value+' varchar(1000))')
	pass


def addBook(cursor,book):
	add(cursor,book.get_name(),book.get_bookID(),book.get_author(),book.get_bookType(),book.get_point(),book.get_briefIntro(),book.get_url())
	pass

def add(cursor,name,bookID,author,bookType,point,briefIntro,url):
	sql ='''insert into book (name, bookID, author, bookType, point, briefIntro, url) values (:name, :bookID, :author, :bookType, :point, :briefIntro, :url)'''
	cursor.execute(sql,{'name':name, 'bookID':bookID, 'author':author, 'bookType':bookType, 'point':point, 'briefIntro':briefIntro, 'url':url})
	cursor.commit()
	pass


def selectByBookID(cursor,bookID):
	cursor.execute('select * from book where bookID=?', (bookID,))
	row = cursor.fetchall()
	return row
	pass


def selectByID(cursor,idE):
	cursor.execute('select * from book where rowid=?', (idE,))
	row = cursor.fetchall()
	return row
	pass

def selectBookID(cursor):
	num = selectNew(cursor)
	result = '0'
	print(num)
	sqlStr= 'select bookID from book where rowid= ?'
	aa=executeSqlGetDict(cursor,sqlStr,str,(num,))
	for data in aa:
		result =  data.get('bookID')
		print(result)
		break
	return result
	pass

def selectNew(cursor):
	result = 0 
	aa = cursor.execute(';select last_insert_rowid() from book;')
	result = aa.lastrowid
	print(result)
	return result
	pass


def executeSqlGetDict(cursor,sqlStr,dataClass,attrList=[]):
    cursor.execute(sqlStr,attrList)
    allData = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    result = []
    for row in allData:
        objDict = {}
        for i in range(0,len(col_names)):
            if type(row[i]) == dataClass:
                objDict[col_names[i]] = str(row[i])[0]  #.split(".")[0]
                continue
            objDict[col_names[i]] = row[i]
        result.append(objDict)
    return result
    pass