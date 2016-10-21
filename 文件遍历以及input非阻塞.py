#coding=utf-8
#遍历文件目录下的所有文件，sep跨平台分割符
import os
s = os.sep
root = ".." + s 
for rt, dirs, files in os.walk(root):
    
	print rt 
	print dirs
	print files  
# print fname
# print new



#基于信号的非阻塞raw_input
import signal

def do_other(signum,frame):
	print 'over'
	exit()  #退出最近的循环体

while True:
	signal.signal(signal.SIGALRM,do_other)
	signal.alarm(5)
	a=raw_input('请输入：')
	print '>>>>>>>>>>>>>'