import datetime
import time
import tkinter as tk

window = tk.Tk()
window.title('DIGITAL CLOCK')
window.configure(background='black')

def clocktime():
  string = time.strftime('%H:%M:%S: %p')
  label.config(text=string)
  label.after(1000, clocktime)

label1 = tk.Label(window, text = "DIGITAL CLOCK", fg= 'green')
label1.pack()

label = tk.Label(window, font=("ds-digital", 35), background="black", foreground="green")
label.pack(anchor= tk.CENTER)
clocktime()
currentdate = datetime.date.today()
date = tk.Label(window, text= currentdate, background="black", foreground="green")
date.pack(anchor= "center")

tk.mainloop()
