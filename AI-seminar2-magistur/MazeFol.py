# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:36:55 2023

@author: Nikolay Shivarov
"""
import numpy as np
import tkinter as tk

maze = np.array([[True, False, True, True, True, True]
                ,[True, True, True, True, True, True]
                ,[True, False, True, False, True, True]
                ,[True, False, True, True, False, True]
                ,[True, True, True, True, False, True]])


rows = len(maze)
cols = len(maze[0])

leftNeighbour = {}
rightNeighbour = {}
upNeighbour = {}
downNeighbour = {}
isCell = {}
isFinal = {(rows-1, cols-1):True}
isStarting = {(0,0):True}
path = {((0,0),""):True }
finalPath = {} 

def checkCell (cell):
    if cell[0]<0 or cell[0]>= rows or cell[1]<0 or cell[1]>=cols or not maze[cell[0]][cell[1]]:
        return False
    return True

for i in range (0,rows):
    for j in range (0,cols):
        if checkCell((i,j)):
            isCell[(i,j)] = True
            upNeighbour[(i,j)] = (i-1,j)
            downNeighbour[(i,j)] = (i+1,j)
            leftNeighbour[(i,j)] = (i,j-1)
            rightNeighbour[(i,j)] = (i,j+1)   

while len(finalPath) == 0:
    newPaths = []
    for p in path:
                if  leftNeighbour[p[0]] in isCell:
                    newPaths.append((leftNeighbour[p[0]], p[1] + "L"))
                    if leftNeighbour[p[0]] in isFinal:
                        finalPath[(leftNeighbour[p[0]],p[1]+"L")] = True
                if  rightNeighbour[p[0]] in isCell:
                    newPaths.append((rightNeighbour[p[0]], p[1] + "R"))
                    if rightNeighbour[p[0]] in isFinal:
                        finalPath[(rightNeighbour[p[0]],p[1]+"R")] = True        
                if  downNeighbour[p[0]] in isCell:
                    newPaths.append((downNeighbour[p[0]], p[1] + "D"))
                    if downNeighbour[p[0]] in isFinal:
                        finalPath[(downNeighbour[p[0]],p[1]+"D")] = True
                if  upNeighbour[p[0]] in isCell:
                    newPaths.append((upNeighbour[p[0]], p[1] + "U"))
                    if upNeighbour[p[0]] in isFinal:
                        finalPath[(upNeighbour[p[0]],p[1]+"U")] = True  
    for p in newPaths:
        path[p] = True                   

print(finalPath)

visited = {}
bPath = {}

def backward (cell, pathsub):
    if len(pathsub)<12:
        if cell in isCell:
            if  leftNeighbour[cell] in isCell:
                if leftNeighbour[cell] in isStarting:
                    rsub = ''.join(reversed(pathsub))
                    bPath["R"+rsub] = True
                else:
                    backward(leftNeighbour[cell], pathsub+"R")
            if  rightNeighbour[cell] in isCell:
                if rightNeighbour[cell] in isStarting:
                    rsub = ''.join(reversed(pathsub))
                    bPath["L"+rsub] = True
                else:
                    backward(rightNeighbour[cell], pathsub+"L")        
            if  downNeighbour[cell] in isCell:
                if downNeighbour[cell] in isStarting:
                    rsub = ''.join(reversed(pathsub))
                    bPath["U"+rsub] = True
                else:
                    backward(downNeighbour[cell], pathsub+"U")
            if  upNeighbour[cell] in isCell:
                if upNeighbour[cell] in isStarting:
                    rsub = ''.join(reversed(pathsub))
                    bPath["D"+rsub] = True
                else:
                    backward(upNeighbour[cell], pathsub+"D")

backward((4,5),"")
root = tk.Tk()
root.title("Backward chaining paths Visualization")

rows = len(maze)
cols = len(maze[0])
cellSize = 40

canvas = tk.Canvas(root, width=cols*cellSize, height=rows*cellSize)
canvas.pack()

# Define colors for cells
wallColor = "red"
pathColor = "black"
cellColor = "lightblue"

def drawMaze():
    for x in range(rows):
        for y in range(cols):       
            if maze[x][y]:
                canvas.create_rectangle(y*cellSize, x*cellSize, (y+1)*cellSize, (x+1) *cellSize, fill=cellColor)
            else:
                canvas.create_rectangle(y*cellSize, x*cellSize, (y+1)*cellSize, (x+1)*cellSize, fill=wallColor)

def drawPath(p):
    root.update()
    root.after(500)
    drawMaze()
    r = 0
    c = 0
    canvas.create_rectangle(c*cellSize, r*cellSize, (c+1)*cellSize, (r+1)*cellSize, fill = pathColor)
    for dir in p:
        if dir == "L":
            c -= 1
        if dir == "R":
            c += 1
        if dir == "U":
            r -= 1
        if dir == "D":
            r += 1   
        canvas.create_rectangle(c*cellSize, r*cellSize, (c+1)*cellSize, (r+1)*cellSize, fill = "yellow")
        root.update()
        root.after(100)    
        canvas.create_rectangle(c*cellSize, r*cellSize, (c+1)*cellSize, (r+1)*cellSize, fill = pathColor)
        root.update()
        root.after(50)
        
def drawPaths():
    root.update()
    root.after(500)
    for p in bPath:
        drawPath(p)

drawPaths()  
root.mainloop()      
                    



