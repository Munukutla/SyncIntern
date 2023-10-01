"""URL SHORTENER PROJECT
FOR SYNC INTERNSHIP"""
from tkinter import *
import pyshorteners
def myurl():
    url=e1.get()
    surl=pyshorteners.Shortener().tinyurl.short(url)
    e2.insert(END,surl)
win=Tk()
win.title("URL shortener using python")
win.geometry("300x200")
win.configure(bg='gray')
Label(win,text="URL SHORTENER USING PYTHON FOR SYNC INTERN'S",bg='black',fg="#FF007F",width="80").pack(pady=10)
l1=Label(win,text="Enter original URL : ",fg='black',bg="#FF007F")
l1.pack()
e1=Entry(win,width="40",bg='black',fg="#FF007F")
e1.pack()
Button(win,text="GENERATE shortend URL LINK",fg='white',bg="#800080",command=myurl).pack()
Label(win,text="shortend URL link:",fg='black',bg="#FF007F").pack()
e2=Entry(win,width="35",bg='black',fg="#FF007F")
e2.pack()

win.mainloop()