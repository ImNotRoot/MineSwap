# -*- coding: utf-8 -*-
from Tkinter import *
from random import *
from time import *

#boton.config(fg='green') Cambiar color de texto en buttons y labels

class Mine:
	col=0
	row=0
	boton=None
	state=0
	def __init__(self,colu,fi,root):
		self.col=colu
		self.row=fi
		boton = Button(root,text=" ")
		boton.grid(row=fi,column=colu)
		
		boton.bind('<Button-1>', self.left)
		boton.bind('<Button-3>', self.right)
		boton.bind('<Button-2>', self.center)
		
	def left(self, event):
		#print str(self.col) + " - " + str(self.row) + " - Izquierdo"
		print self.state
		
	def right(self, event):
		print str(self.col) + " - " + str(self.row) + " - Derecho"
		print self.state
		
	def center(self, event):
		print str(self.col) + " - " + str(self.row) + " - Central"
		print self.state
	
	def getState(self):
		return self.state
	
	def setState(self,value):
		self.state=value

def fillMines(board,col,fil,num):
	for c in range(num):
		flag = True
		while flag:
			randcol=randint(0,col-1)
			randfil=randint(0,fil-1)
			if(board[randcol][randfil].getState()!=-1):
				board[randcol][randfil].setState(-1)
				flag = False
	
root = Tk()
root.title('MineSwap')
root.geometry("800x590")
root.resizable(0,0)
panel=Frame(root)

counter = Label(panel, text="000 <-Contador")
counter.pack(side=LEFT)
restart=Button(panel, text="( ͡° ͜ʖ ͡°)")
restart.pack(side=LEFT,expand=True)
time = Label(panel, text="Tiempo-> 000")
time.pack(side=RIGHT)

panel.pack(side=TOP,fill=BOTH)

board=[]
game=Frame(root)
for c in range(20):
	row=[]
	for f in range(20):
		mine=Mine(c,f,game)
		row.append(mine)
	board.append(row)

fillMines(board,20,20,100)

for c in range(20):
	a=""
	for i in range(20):
		if(board[i][c].getState()==-1):
			a = a +  str(board[i][c].getState())
		else:
			a = a + " " + str(board[i][c].getState())
	print a

game.pack(side=BOTTOM,fill=BOTH)

root.mainloop()
