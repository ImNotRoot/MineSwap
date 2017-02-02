#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getArround(array,col,row,limc,limr):
	for c in range(col-1,col+2):
		if(c>=0 and c<limc):
			for i in range(row-1,row+2):
				if(i>=0 and i<limr):
					print str(array[i][c])

LEN=10

cont=0

array=[]

for c in range(LEN):
	row=[]
	for i in range(LEN):
		row.append(cont)
		cont=cont+1
	array.append(row)
	

for c in range(LEN):
	print array[c]
	
getArround(array,5,4,LEN,LEN)
