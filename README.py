from heapq import heappush, heappop 
import math
from math import sqrt
import time
import random
import xlrd
from Tkinter import *
file_location1 ="/home/raaghav/Desktop/pleasework.xls"
workbook1 = xlrd.open_workbook(file_location1)
sheet1 = workbook1.sheet_by_index(0)
data1 = [[sheet1.cell_value(r,c) for c in range(sheet1.ncols)] for r in range (sheet1.nrows)]


class node:
    xPos = 0 
    yPos = 0 
    distance = 0
    priority = 0 
    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10
    
    def nextMove(self, dirs, d): 
        if dirs == 8 and d % 2 != 0:
            self.distance += 99999
        else:
            self.distance += 10
   
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos         
       
        d = (sqrt(xd*xd + yd*yd))
    
        return(d)

def pathFind(the_map, n, m, dirs, dx, dy, xA, yA, xB, yB):
    closed_nodes_map = [] 
    open_nodes_map = [] 
    dir_map = [] 
    row = [0] * n
    for i in range(m):
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []]
    pqi = 0 
    n0 = node(xA, yA, 0, 0)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority 

    while len(pq[pqi]) > 0:
        
        n1 = pq[pqi][0] 
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) 
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 

        
        if x == xB and y == yB:
            
            path = ''
            while not (x == xA and y == yA):
                j = dir_map[y][x]
                c = str((j + dirs / 2) % dirs)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        for i in range(dirs):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xB, yB)
               
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    
                    dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    
                    open_nodes_map[ydy][xdx] = m0.priority
                   
                    dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                    
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi])
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])       
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) 
    return '' 

dirs = 4
if dirs == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif dirs == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

the_map1=[]
l=0
n=1
while(data1[n][7]==0):
    if(data1[n][6]>l and (data1[n][2]==90 or data1[n][2]==270)):l=data1[n][6]
    n=n+1
for m in range(n):
    if(data1[m][6]==l and (data1[n][2]==90 or data1[n][2]==270)):break
height1 = int(l)
print height1
width1 = int(abs(data1[sheet1.nrows-1][7]))
print width1
row = [0] * width1
for i in range(height1): # create empty map
    the_map1.append(list(row))


for i in range (1,sheet1.nrows):
    if(i==m):continue
    if ( data1[i][2]==90 or data1[i][2]==270):
	        for j in range (int(data1[i][7])+1,width1):
	      	  for k in range (int(min(data1[i][4],data1[i][8])),int(max(data1[i][4],data1[i][8]))):
	        	    #self.cells[int((j-1)*l+k)].reachable=not self.cells[int((j-1)*l+k)].reachable
	        	   if the_map1[k][j-1] ==1 :
	                   	the_map1[k][j-1] =0
	       	   	   else  :
	                 	 the_map1[k][j-1] =1
master = Tk()
master.title(" Academic Building 1st Floor ")	
w = Canvas(master, width=1000, height=700)
for i in range (1,sheet1.nrows):
	w.create_line(20+data1[i][7], 600-data1[i][8],20+data1[i][3],600-data1[i][4], fill="Black", width=2)
w.pack()
#for i in range(width1):
#	for j in range( height1 ):
#		if(the_map1[j][i]==1):
#			w.create_rectangle(20+i,600-j,20+i,600-j, outline = "LightBlue")
start_pt = w.create_text(200,620, anchor="nw",font=("Purissa",30), fill = "Green")
end_pt = w.create_text(650,620, anchor="nw",font=("Purissa",30), fill = "Red")
canvas_id= w.create_text(20, 50, anchor="nw",font=("Purissa",20), fill = "DarkBlue")
w.create_rectangle(150,628,180,658, fill = "Green")
w.create_rectangle(600,628,630,658, fill = "Red")
w.itemconfig(start_pt, text="Source")
w.itemconfig(end_pt, text="Destination")
w.itemconfig(canvas_id, text = "Left click to set Starting Point                    Right click to set Ending Point")
x1=0 
y1=0
oval= 0

def upon_Lclick(event):
	
	print " left clicked"
	global x1
	global y1
	global oval
	if (oval is not 0):w.delete( oval )
	x1= event.x
	y1=event.y
	oval =w.create_oval( x1-5 , y1-5,x1+5,y1+5, fill = "Red",outline = "Red")
	w.itemconfigure(canvas_id, state ='hidden')	

def upon_Rclick(event):
	global oval
	print " right clicked"

	( xB , yB ) = ( event.x , event.y )
	w.create_oval( xB-5 , yB-5,xB+5,yB+5, fill = "Yellow" ,outline = "Yellow")
	xA = x1
	yA = y1
	xA = xA-20
	xB = xB -20
	yA = 600- yA
	yB = 600 - yB
	
	if( xA > width1 or xA < 0 or xB > width1 or xB < 0 or yA > height1 or yA<0 or yB > height1 or yB < 0): 
		w.itemconfigure(canvas_id, state = 'normal')	
		w.itemconfig(canvas_id, text="                            Please think before you act :/")
		w.update_idletasks()
		w.after(1000)

	elif (the_map1[yA][xA]==1 or the_map1[yB][xB] == 1):
		w.itemconfigure(canvas_id, state = 'normal')	
	        w.itemconfig(canvas_id, text="                                       That is a wall -_-")
		w.update_idletasks()
		w.after(1000)

	else :
		route = pathFind(the_map1, width1, height1, dirs, dx, dy, xA, yA, xB, yB)	
		print "solved"
		
		for i in route:
			xB = xA + dx[int(i)]
			yB = yA + dy[int(i)]
			w.create_line( 20+xA, 600-yA, 20+xB, 600-yB,fill ="Green" , width = 1)
			w.update_idletasks()
			w.after(5)
			xA= xB
			yA= yB
	oval=0
	w.itemconfigure(canvas_id, state = 'normal')	
	w.itemconfig(canvas_id, text ="Left click to set Starting Point                    Right click to set Ending Point")
def re():
	w.delete("all")
	for i in range (1,sheet1.nrows):
		w.create_line(20+data1[i][7], 600-data1[i][8],20+data1[i][3],600-data1[i][4], fill="Black", width=2)
	w.create_rectangle(150,628,180,658, fill = "Green")
	w.create_rectangle(600,628,630,658, fill = "Red")
	global canvas_id
	canvas_id = w.create_text(20, 50, anchor="nw",font=("Purissa",20), fill = "DarkBlue")
	start_pt = w.create_text(200,620, anchor="nw",font=("Purissa",30), fill = "Green")
	end_pt = w.create_text(650,620, anchor="nw",font=("Purissa",30), fill = "Red")
	w.itemconfig(start_pt, text="Source")
	w.itemconfig(end_pt, text="Destination")
	w.itemconfig(canvas_id, text = "Left click to set Starting Point                    Right click to set Ending Point")

w.bind("<Button-1>",  upon_Lclick)
w.bind("<Button-3>", upon_Rclick)
w.pack()
b = Button(master, text="Reload Map", command=re)
b.configure(width = 10, activebackground = "Yellow", background ="#33B5E5", relief = FLAT)
b.pack()

mainloop()




raw_input('Press Enter...')
