#! /usr/bin/env python

import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text='Hello World!')
quit = Tkinter.Button(top, text='quit', command=top.quit)
label.pack()
quit.pack()
Tkinter.mainloop()
