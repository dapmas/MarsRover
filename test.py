from itertools import izip

def pairwise(iterable):
    a = iter(iterable)
    return izip(a , a)

direction = 'NESW'

delta_moves = [(0,1),(1,0),(0,-1),(-1,0)]

def rotate_right(action):
    return (action+1) % 4

def rotate_left(action):
    return ((action-1)+4) % 4

def move(x,y,action):
    return x+delta_moves[action][0], y+delta_moves[action][1]



testcase_file = open("testcase.txt",'r')
testcase = [line.strip().split() for line in testcase_file if not line.startswith(('#')) and line.strip()]


Grid = testcase[0]

testcase = testcase[1:]


for startingPoint, instructions in pairwise(testcase):
    x, y , dir = startingPoint
    pos = [int(x), int(y), direction.find(dir)]

    if (pos[0] < 0 or pos[0] > int(Grid[0]) or pos[1] < 0 or pos[1] > int(Grid[1]) or pos[2] == -1) :
        print "Invalid Usecase"
        continue

    instn = str(instructions).lower()

    for i in instn:
        if(i=='r'):
            pos[2] = rotate_right(pos[2])

        if(i=='l'):
            pos[2] = rotate_left(pos[2])

        if(i=='m'):
            pos[0], pos[1] = move(pos[0],pos[1],pos[2])

    if (pos[0] > int(Grid[0]) or pos[1] > int(Grid[1]) or pos[0] < 0 or pos[1] < 0):
        print "Rover Moving out of Plateau : Invalid Instruction Set"

    else:
        print pos[0], pos[1], direction[pos[2]]
