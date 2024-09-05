# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:18:04 2023

@author: Nikolay Shivarov
"""

import numpy as np
from queue import PriorityQueue
import tkinter as tk

maze = np.array([[True, False, True, True, True, True]
                ,[True, True, True, True, True, True]
                ,[True, False, True, False, True, True]
                ,[True, False, True, True, False, True]
                ,[True, True, True, True, False, True]])


rows = len(maze)
cols = len(maze[0])

cellSize = 40


root = tk.Tk()
root.title("A* Visualization")


canvas = tk.Canvas(root, width=cols*cellSize, height=rows*cellSize)
canvas.pack()

# Define colors for cells
wallColor = "red"
notVisitedColor = "lightblue"
visitedColor = "green"
outOfTheQueueColor = "yellow"
pathColor = "black"   


class cellNode:
     row = 0
     col = 0
     path = ""
     def __init__(self, row, col, path):
        self.row = row
        self.col = col
        self.path = path
     def manhattan(self):
         return rows - self.row + cols - self.col - 2 
     def colorVisited(cn):
         canvas.create_rectangle(cn.col*cellSize, cn.row*cellSize, (cn.col+1)*cellSize, (cn.row+1)*cellSize, fill = visitedColor)
         root.update()
         root.after(500)
     
     def cost(self):
         return len(self.path)
     
     def h(self):
         return self.cost() + self.manhattan()
    
     def isFinal (self):
         return self.row == rows-1 and self.col == cols-1 
     
     def __lt__(self, other):
        return self.h() < other.h()

     def printInside(self):
        print ("Going into the queue: row:", self.row, "col:", self.col)

     def printOutside(self):
        print ("Going out of the queue: row:", self.row, "col:", self.col)
     def drawPath(self):
         r = 0
         c = 0
         canvas.create_rectangle(c*cellSize, r*cellSize, (c+1)*cellSize, (r+1)*cellSize, fill = pathColor)
         root.update()
         root.after(500)
         for dir in self.path:
             if dir == "L":
                 c -= 1
             if dir == "R":
                 c += 1
             if dir == "U":
                 r -= 1
             if dir == "D":
                 r += 1   
             canvas.create_rectangle(c*cellSize, r*cellSize, (c+1)*cellSize, (r+1)*cellSize, fill = pathColor)
             root.update()
             root.after(500)    
                 

def loadQueue (q, cn, visited):
    if cn.col>0 and maze[cn.row][cn.col-1] and not visited[cn.row][cn.col-1]:
       path = cn.path + 'L'
       leftCn = cellNode(cn.row, cn.col-1, path)
       q.put(leftCn)
       visited[cn.row][cn.col-1] = True
       leftCn.printInside()
       leftCn.colorVisited()
    if cn.col < cols-1  and maze[cn.row][cn.col+1] and not visited[cn.row][cn.col+1]:
       path = cn.path + 'R'
       rightCn = cellNode(cn.row, cn.col+1, path)
       q.put(rightCn)
       visited[cn.row][cn.col+1] = True
       rightCn.printInside()
       rightCn.colorVisited()
    if cn.row>0 and maze[cn.row-1][cn.col] and not visited[cn.row-1][cn.col]:
       path = cn.path + 'U'
       upCn = cellNode(cn.row-1, cn.col, path)
       q.put(upCn)
       visited[cn.row-1][cn.col] = True
       upCn.printInside()
       upCn.colorVisited()
    if cn.row<rows-1  and maze[cn.row+1][cn.col] and not visited[cn.row+1][cn.col]:
       path = cn.path + 'D'
       downCn = cellNode(cn.row+1, cn.col, path)
       q.put(downCn)  
       visited[cn.row+1][cn.col] = True
       downCn.printInside()
       downCn.colorVisited()

     
def aStar():
   visited = np.zeros((rows, cols), dtype=bool)
   pq = PriorityQueue()
   pq.put(cellNode(0, 0, ""))
   visited[0][0] = True
   while not pq.empty():
       cn = pq.get()
       cn.printOutside()
       canvas.create_rectangle(cn.col*cellSize, cn.row*cellSize, (cn.col+1)*cellSize, (cn.row+1)*cellSize, fill = outOfTheQueueColor)
       root.update()
       root.after(500)
       if cn.isFinal():
           print(cn.path)
           print(cn.cost())
           cn.drawPath()
           break
       loadQueue(pq, cn, visited)

#drawing the maze before the algorithm starts
for x in range(rows):
    for y in range(cols):       
        if maze[x][y]:
            canvas.create_rectangle(y*cellSize, x*cellSize, (y+1)*cellSize, (x+1) *cellSize, fill=notVisitedColor)
        else:
            canvas.create_rectangle(y*cellSize, x*cellSize, (y+1)*cellSize, (x+1)*cellSize, fill=wallColor)    
       
    
aStar()        

root.mainloop()

