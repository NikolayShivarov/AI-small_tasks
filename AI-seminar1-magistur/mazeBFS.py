# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:31:37 2023

@author: Nikolay Shivarov
"""

import numpy as np
from queue import Queue



maze = np.array([[True, False, True, True, True, True]
                ,[True, True, True, True, True, True]
                ,[True, False, True, False, True, True]
                ,[True, False, True, True, False, True]
                ,[True, True, True, True, False, True]])


rows = len(maze)
cols = len(maze[0])


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

def loadQueue (q, cn, visited):
    if cn.col>0 and maze[cn.row][cn.col-1] and not visited[cn.row][cn.col-1]:
       path = cn.path + 'L'
       leftCn = cellNode(cn.row, cn.col-1, path)
       q.put(leftCn)
       visited[cn.row][cn.col-1] = True
       leftCn.printInside()
    if cn.col < cols-1  and maze[cn.row][cn.col+1] and not visited[cn.row][cn.col+1]:
       path = cn.path + 'R'
       rightCn = cellNode(cn.row, cn.col+1, path)
       q.put(rightCn)
       visited[cn.row][cn.col+1] = True
       rightCn.printInside()
    if cn.row>0 and maze[cn.row-1][cn.col] and not visited[cn.row-1][cn.col]:
       path = cn.path + 'U'
       upCn = cellNode(cn.row-1, cn.col, path)
       q.put(upCn)
       visited[cn.row-1][cn.col] = True
       upCn.printInside()
    if cn.row<rows-1  and maze[cn.row+1][cn.col] and not visited[cn.row+1][cn.col]:
       path = cn.path + 'D'
       downCn = cellNode(cn.row+1, cn.col, path)
       q.put(downCn)  
       visited[cn.row+1][cn.col] = True
       downCn.printInside()

def bfs():
    visited = np.zeros((rows, cols), dtype=bool)
    q = Queue(maxsize = rows * cols )
    q.put(cellNode(0, 0, ""))
    visited[0][0] = True
    while not q.empty():
        cn = q.get()
        cn.printOutside()
        if cn.isFinal():
            print(cn.path)
            print(cn.cost())
            break
        loadQueue(q, cn, visited)


   
bfs()     
 

       
      
       


