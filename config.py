#!/usr/bin/env python3    
# -*- coding: utf-8 -*-

 
# 数据库名称
db_path = 'book.db'
# 邮箱参数
mail_host = "smtp.163.com"      
mail_user = "************@163.com"                
mail_pass = "*********"          
 
mail_sender = mail_user   
mail_receivers = ['***************@qq.com']  
 #获取下载地址
def getUrl(num):
	return 'http://www.*********.com/'+num+'.html'
	pass
# 保存最新下载记录的文件
Down_Num = 'num.txt'