'''
Created on 12-Jul-2015

@author: behroz
'''
import numpy as np
import random
import grid

def find_y(x,R):
    y_lst = []
    for y in range(0,R.shape[0]):
        if R[x][y] != -1 :
            y_lst.append(y)
    return random.choice(y_lst)

def find_next_Qmax(y,Q):
    next_action_lst = []
    for i in range(0,Q.shape[0]):
        if Q[y][i]!=-1:
            next_action_lst.append(Q[y][i])
    return max(next_action_lst)

def q_learning2(Q,R,gma):
    for i in range(0,600):
        x = random.randint(0,R.shape[0]-1)
        reward = 0
        while reward != 100:
            y = find_y(x,R)
            next_Qmax = find_next_Qmax(y, Q)
            Q[x][y] = R[x][y] + gma*next_Qmax
            reward = R[x][y]
            x = y
    return Q

def find_max_index(Q):
    max_index = 0
    for i in range(0,Q.shape[0]):
        if Q[i] > Q[max_index]:
            max_index = i
    return max_index

def find_path(Q,state):
    path = []
    state = state
    while state!=15:
        path.append(state)
        state = find_max_index(Q[state])
    path.append(15)
    return path

def color_path(lst):
    i=0
    while True:
        if i < len(lst):
            grid.canvas.itemconfig(grid.grid[lst[i]], fill="green")
            i = i + 1
        grid.root.update()

R = np.array([[-1]*16]*16)
R[1][0]=0
R[0][1]=0
R[0][4]=0
R[4][0]=0
R[4][8]=0
R[8][4]=0
R[8][9]=0
R[8][12]=0
R[12][8]=0
R[9][8]=0
R[9][5]=0
R[9][10]=0
R[9][13]=0
R[10][14]=0
R[10][9]=0
R[14][10]=0
R[14][13]=0
R[13][14]=0
R[13][9]=0
R[5][9]=0
R[5][6]=0
R[6][2]=0
R[6][5]=0
R[2][3]=0
R[2][6]=0
R[3][2]=0
R[3][7]=0
R[7][3]=0
R[7][11]=0
R[11][7]=0
R[11][15]=100
R[15][11]=0
R[15][15]=100

Q = np.array([[0]*16]*16)
Q = q_learning2(Q, R, 0.9)
print(Q)
path = find_path(Q, 1)
print(path)
color_path(path)
