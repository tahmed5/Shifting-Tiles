import random
import time
import pprint
import numpy
from copy import copy 
'''
aList = [[1,2,3],[5,6,7]]

print(aList[0][2])

Dict = {}

Dict[0] = aList

for item in Dict.values():
    print(item)
    if item == aList:
        print('Same')
'''

class Tree:
    pass

def log_move(str_value, direction):
    if str_value not in log.keys():
        log[str_value] = []

    if direction not in log[str_value]:
        log[str_value].append(direction)
    
def create_grid():
    global size
    global zero_x
    global zero_y
    grid = []
    acceptable_size = False
    
    while acceptable_size != True:
        size = int(input('Enter the length of the grid\n'))
        if size > 1:
            acceptable_size = True
            
    numbers = list(range(0,size ** 2))
    
    for y in range(size):
        grid.append([])
        for x in range(size):
            value = random.choice(numbers)
            if value == 0:
                zero_x = x
                zero_y = y
            grid[y].append(value)
            numbers.remove(value)
    
            
    print('The Starting Grid Is:')
    for row in grid:
        print(row)
    print(grid)
    print('With Zero lying on the point', '(' + str(zero_x) + ',' + str(zero_y) + ')')

    return grid 
def str_value(grid):
    grid1d = []
    str_grid = None
    for row in grid:
        for column in row:
            grid1d.append(str(column))

    str_grid = ''.join(grid1d)

    return str_grid
    
def grid_connections(parent,child):
    
    parent_str = str_value(parent)
    
    child_str = str_value(child)

    time.sleep(5)
    
    if parent_str not in connections.keys():
        connections[parent_str] = []

    if child_str not in connections[parent_str]:
        connections[parent_str].append(child_str)

    
def target():
    perfect_grid = []
    numbers = list(range(0, size**2))
    
    for y in range(size):
        perfect_grid.append([])
        for x in range(size):
            perfect_grid[y].append(numbers.pop(0))

def unique_grid(grid):
    global grid_id
    global grid_key
    unique = False
    
    str_grid = str_value(grid)
    
    if str_grid not in grid_key.values():
        unique = True
        grid_id += 1
        grid_key[grid_id] = str_grid

    if str_grid == '012345678':
        pprint.pprint(grid_key)
        quit()
        
    return unique

def move(grid):
    global zero_x
    global zero_y
    x,y = zero_x, zero_y
    temp_grid = grid
    print(grid,'g')
    moves = ['U','D','L','R']

    if x == 0:
        moves.remove('L')
    if y == 0:
        moves.remove('U')
    if x == (size - 1):
        moves.remove('R')
    if y == (size - 1):
        moves.remove('D')
        

    direction = random.choice(moves)
    
    if direction == 'U':
        
        swap = temp_grid[y-1][x] #holds the value that is going to be swapped with zero
        temp_grid[y-1][x] = 0
        temp_grid[y][x] = swap
        zero_y = zero_y - 1 ]
        
    if direction == 'D':
        swap = temp_grid[y+1][x] #holds the value that is going to be swapped with zero
        temp_grid[y+1][x] = 0
        temp_grid[y][x] = swap
        zero_y = zero_y + 1         
        
    if direction == 'L':
        swap = temp_grid[y][x-1] #holds the value that is going to be swapped with zero
        temp_grid[y][x-1] = 0
        temp_grid[y][x] = swap
        zero_x = zero_x - 1
        
    if direction == 'R':
        swap = temp_grid[y][x+1] #holds the value that is going to be swapped with zero
        temp_grid[y][x+1] = 0
        temp_grid[y][x] = swap
        zero_x = zero_x + 1

    print(temp_grid,'t')
    print(grid,'g2')
    print()
    time.sleep(3)
    if unique_grid(temp_grid) == True:
        log_move(str_value(temp_grid), direction)
        grid = temp_grid
        
    return grid

def create_tree():
    global grid_key
    global grid_id
    global log
    global connections
    grid = create_grid()
    goal = target()
    grid_key = {}
    connections = {}
    log = {}
    grid_id = 0
    grid1d = []
    str_grid = None
    for row in grid:
        for column in row:
            grid1d.append(str(column))

    str_grid = ''.join(grid1d)

    print(str_grid)
            
            
    grid_key[grid_id] = str_grid

    start_grid = grid
    
    goal_reached = False

    while goal_reached != True:
        grid = move(grid)
        
    
def main():
    create_tree()


main()
