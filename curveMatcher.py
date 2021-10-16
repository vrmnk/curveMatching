'''
#create application
from tkinter import *

#create canvas
my_window =Tk()
my_canvas = Canvas (my_window, width=1000, height=1000, background='white')
my_canvas.grid(row=0,column=0)
#create line
my_canvas.create_line(0,1000,1000,,fill='red')
my_window.mainloop()
'''
import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y

def draw_line(event):

    if str(event.type) == 'ButtonPress':
        canvas.old_coords = event.x, event.y

    elif str(event.type) == 'ButtonRelease':
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)

def reset_coords(event):
    canvas.old_coords = None

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

root.bind('<ButtonPress-1>', draw_line)
root.bind('<ButtonRelease-1>', draw_line)

#root.bind('<B1-Motion>', draw)
#root.bind('<ButtonRelease-1>', reset_coords)

root.mainloop()