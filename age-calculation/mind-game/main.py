
from tkinter import *

win = Tk()

r, c = win.maxsize()
win.geometry(f'{r//2}x{c//2}')
lst = iter([[2, 3, 4, 5, 5], [3, 4 ,3], [4, 5, 3 ], 0])
out = []
l1 = Label(win, text=f"{next(lst)}", )
l1.pack()

# win.grid()

def click1():
        global out
        x = next(lst)
        if x == 0:
            l1.config(text=f'{"".join(out)}')
        else:    
            l1.config(text=f'{x}')
        out.append('1')

def click2():
            l1.config(text=f'{next(lst)}')
            global out
            x = next(lst)
            l1.config(text=f'{x}')
            out.append('0')

l2 = Button(win, text="Yes", bg='red', command=click1)
l2.pack()

l3 = Button(win, text="No", command=click2)
l3.pack()


win.mainloop()