#!/usr/bin/env python3   
# -*- coding: utf-8 -*-

from enum import Enum
# Book=Enum('Book',('name','bookID','author','bookType','point','briefIntro','url'))

class Book(Enum):
	name='name'
	bookID='bookID'
	author='author'
	bookType='bookType'
	point='point'
	briefIntro='briefIntro'
	url='url'

class BookBean(object):
	def __init__(self, name, bookID,author,bookType,point,briefIntro,url):
		self.name=name
		self.bookID=bookID
		self.author=author
		self.bookType=bookType
		self.point=point
		self.briefIntro=briefIntro
		self.url=url

	def get_name(self):
		return self.name

	def set_name(self,name):
		self.name=name
		pass

	def get_bookID(self):
		return self.bookID

	def set_bookID(self,bookID):
		self.bookID=bookID
		pass

	def get_author(self):
		return self.author

	def set_author(self,author):
		self.author=author
		pass

	def get_bookType(self):
		return self.bookType

	def set_bookType(self,bookType):
		self.bookType=bookType
		pass

	def get_point(self):
		return self.point

	def set_point(self,point):
		self.point=point
		pass

	def get_briefIntro(self):
		return self.briefIntro

	def set_briefIntro(self,briefIntro):
		self.briefIntro=briefIntro
		pass

	def get_url(self):
		return self.url
	
	def set_url(self,url):
		self.url=url
		pass

	def __str__(self):
		return "name="+self.name+"|"+"bookID="+self. bookID+"|"+"author="+self.author+"|"+"bookType="+self.bookType+"|"+"point="+self.point+"|"+"briefIntro="+self.briefIntro+"|"+"url="+self.url

# print(dir(Book.name))
# ['__class__', '__doc__', '__module__', 'value']

# print(Book.name.value)
# name

# print(Book.__name__)
# Book