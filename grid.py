'''
Created on 12-Jul-2015

@author: behroz
'''
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root,width=800,height=600)
canvas.pack()

grid = [0]*16
y=50
r=20
counter = 0
for i in range(0,4):
    x=200
    for j in range(0,4):
        grid[counter] = canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue")
        counter = counter+1
        x = x + 2*r+100
    y = y + 2*r+100

c = []
for i in range(0,16):
    c.append(canvas.coords(grid[i]))

def point(c):
    return ((c[0]+c[2])/2,(c[1]+c[3])/2)

canvas.create_line(point(c[0]),point(c[4]),fill='red',width=5)
canvas.create_line(point(c[1]),point(c[0]),fill='red',width=5)
canvas.create_line(point(c[4]),point(c[8]),fill='red',width=5)
canvas.create_line(point(c[8]),point(c[12]),fill='red',width=5)
canvas.create_line(point(c[8]),point(c[9]),fill='red',width=5)
canvas.create_line(point(c[12]),point(c[8]),fill='red',width=5)
canvas.create_line(point(c[9]),point(c[5]),fill='red',width=5)
canvas.create_line(point(c[9]),point(c[13]),fill='red',width=5)
canvas.create_line(point(c[9]),point(c[10]),fill='red',width=5)
canvas.create_line(point(c[9]),point(c[8]),fill='red',width=5)
canvas.create_line(point(c[10]),point(c[9]),fill='red',width=5)
canvas.create_line(point(c[10]),point(c[14]),fill='red',width=5)
canvas.create_line(point(c[14]),point(c[13]),fill='red',width=5)
canvas.create_line(point(c[13]),point(c[9]),fill='red',width=5)
canvas.create_line(point(c[5]),point(c[9]),fill='red',width=5)
canvas.create_line(point(c[5]),point(c[6]),fill='red',width=5)
canvas.create_line(point(c[6]),point(c[2]),fill='red',width=5)
canvas.create_line(point(c[6]),point(c[5]),fill='red',width=5)
canvas.create_line(point(c[2]),point(c[3]),fill='red',width=5)
canvas.create_line(point(c[2]),point(c[6]),fill='red',width=5)
canvas.create_line(point(c[3]),point(c[2]),fill='red',width=5)
canvas.create_line(point(c[3]),point(c[7]),fill='red',width=5)
canvas.create_line(point(c[7]),point(c[3]),fill='red',width=5)
canvas.create_line(point(c[7]),point(c[11]),fill='red',width=5)
canvas.create_line(point(c[11]),point(c[7]),fill='red',width=5)
canvas.create_line(point(c[11]),point(c[15]),fill='red',width=5)

for i in grid:
    canvas.tag_raise(i)

text_array= [0]*16
for i in range(0,16):
    text_array[i] = canvas.create_text(point(c[i]),font=('Arial',20),fill='black')
    canvas.itemconfigure(text_array[i], text=str(i))
    
canvas.itemconfig(grid[-1], fill="red")
