import tkinter as tk

from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def time():
    string=strftime(" Digital Clock \n \n %H:%M:%S %p \n %d-%m-%Y")
    label.config(text=string)
    label.after(1000,time)

label =tk.Label(root,font=("calibri",60,"bold") , bg="white", fg="black",padx=200, pady=200)
label.pack(anchor="center")

time()
root.mainloop()
