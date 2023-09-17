import datetime
from tkinter import *
import time
import tkinter.font
from tkinter import messagebox
import winsound
from threading import *
win=Tk()
win.title("Alarm Clock")
win.geometry("300x200")
win.configure(bg="#FF007F")


def Threading():
	t1=Thread(target=alarm)
	t1.start()


def alarm():
		# Infinite Loop
	while True:
			# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

			# Wait for one seconds
		#time.sleep(1)

			# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time, set_alarm_time)

			# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
				# Playing sound
			winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
			messagebox.showinfo(title="WakeUp", message="GOOD MORNING,\n its time to wake up")
			break



def time():
	current_time=StringVar(win)
	current_time=datetime.datetime.now().strftime("%H:%M:%S:%p")
	lbl.configure(text=current_time)
	lbl.after(1000,time)
lbl=Label(win,font=tkinter.font.Font(family="calibbri",size=60,weight="bold"),bg="#0AFFFF",fg="#52595D")
lbl.pack(anchor='center')
time()

#widgets on tkinter
Label(win,text="Alarm to set Time",fg="#7D0552",bg="#FFB2D0",font=tkinter.font.Font(family="Comic Sans MS",size=25,weight="bold")).pack(pady=10)
lab1=Label(win,text="HOURS",bg="#006400",fg="white",font=tkinter.font.Font(size=22))
lab1.pack()
hour=StringVar(win)
tf1=Entry(win,textvariable=hour)
tf1.pack()
lab2=Label(win,text="MINUTES",bg="#006400",fg="white",font=tkinter.font.Font(size=22))
lab2.pack()
minute=StringVar(win)
tf2=Entry(win,textvariable=minute)
tf2.pack()
lab3=Label(win,text="SECONDS",bg="#006400",fg="white",font=tkinter.font.Font(size=22))
lab3.pack()
second=StringVar(win)
tf3=Entry(win,textvariable=second)
tf3.pack()
but2=Button(win,fg="white",bg="#0000A0",text="SET THIS TIME",font=tkinter.font.Font(size=22),command=Threading)
but2.pack(padx=5,pady=5)
time()


win.mainloop()