#  tkinter 



from tkinter import *



win = Tk()
r, c =  win.maxsize()
win.geometry(f"{r//2}x{c//2}")

win.resizable(False, False)

# win.configure(bg='black')
win.configure(bg='#328322')
# print(win.maxsize())

win.mainloop()