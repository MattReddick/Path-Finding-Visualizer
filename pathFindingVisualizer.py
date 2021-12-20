import pyglet
from pyglet.window import key
import random
import math, time

window = pyglet.window.Window(fullscreen=True)
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent',)
window.maximize()
colorChoice = [random.randint(0,25), random.randint(0,25), random.randint(0,25)]
w, h = 28, 14;
matrix = [[0 for x in range(w)] for y in range(h)]
values = [[[-1, -1] for x in range(w)] for y in range(h)]

location = [7, 13]
checked = [[50, 50], [50, 50]]
counter = [0,2]
priorStart = [50, 0]
priorEnd = [50, 1]
label = pyglet.text.Label(' Path Finding Algorithm', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height - 20, anchor_x='center', anchor_y='center')
keys = pyglet.text.Label('SPACE: create wall or undo block    S: create start block   E: create end block   R: reset screen   ENTER: find path', font_name='Times New Roman', font_size=20, x=window.width//2, y=15, anchor_x='center', anchor_y='center')


def findPath(cy, cx):
    ey = endLoc[0]
    ex = endLoc[1]
    middle = [cy,cx]
    goal = [ey,ex]
    checked.append(middle)

    while (middle != goal) and counter[0] < 390:
        for row in range(-1, 2):
            for column in range(-1, 2):
                currentNode = [row, column]
                print('cx ' + str(cx) + ' cy ' + str(cy) + '  row ' + str(row) + '  column ' + str(column) + '  ex  ' + str(ex) + '   ey  ' + str(ey))
                '''print('1. ' + str(cx + row) + '  2.' + str(cy+column) + '  3. ' + str(values[row][column]))'''
                if (cx + row != -1) and (cx+row != 28) and (cy + column != -1) and (cy + column != 14 ):
                    print('1. ' + str(cx + row) + '  2.' + str(cy+column))
                    if currentNode != [0, 0]:
                        if values[cy+column][cx+row] != [-2, -2]:
                            values[cy+column][cx+row] = [int(10*math.sqrt((math.pow((column+cy)-ey, 2)) + (math.pow((row+cx)-ex, 2)))), int(10*math.sqrt((math.pow((column+cy)-cy, 2)) + (math.pow((row+cx)-cx, 2))))]
                            #print(values[cy+column][cx+row])
                            if (matrix[cy+column][cx+row][0] + matrix[cy+column][cx+row][1] + matrix[cy+column][cx+row][2]) < 100:
                                matrix[cy+column][cx+row] = [190, 190, 50]
                            '''if counter[0] > 0:
                                if (values[priorNode[0]][priorNode[1]][0] + values[priorNode[0]][priorNode[1]][1]) < (values[cx][cy][0] + values[cx][cy][1]):
                                    matrix[priorNode[0]][priorNode[1]] = [250, 250, 0]'''
                print((cx + row != -1) + (cx + row != 15) + (cy + column != -1) + (cy + column != 29))
        '''print(values)'''
        node = lowestValue()
        priorNode = [cy, cx]
        '''node = diagonal(node)'''
        cx = node[1]
        cy = node[0]
        middle = [cy, cx]
        if middle != goal:
            matrix[node[0]][node[1]] = [0, 0, 220]




        counter[0] += 1
        #matrix[cy][cx] = [0, 0, 0]
    '''print(middle!= goal)
    print(counter[0])'''


def lowestValue():
    lowest = 1999999
    lowestNode = [0, 0]

    for j in range (28):
        for i in range(14):
            if values[i][j] != [-1,-1] and values[i][j] != [-2,-2]:
                if ((values[i][j][0] + values[i][j][1]) < lowest) and [i, j] not in checked:
                    lowest = values[i][j][0] + values[i][j][1]
                    lowestNode = [i, j]
    checked.append(lowestNode)
    return lowestNode


def diagonal(node):
    for j in range(-1, 2):
        for i in range(-1, 2):
            if values[node[0] + i][node[1] + j] == [-1, -1]:
                if (j == -1 and i == -1) or (j == 2 and i == 2) or (j == 2 and i == -1) or (j == -1 and i == 2):
                    openDistance = 14
                else:
                    openDistance = 10
                if int(10*math.sqrt((math.pow((node[0])-startLoc[0], 2)) + (math.pow((node[1])-startLoc[1], 2) + openDistance))) < int(10*math.sqrt((math.pow((i+node[0])-startLoc[0], 2)) + (math.pow((j+node[1])-startLoc[1], 2)))):
                    return [i+ node[0],j+node[1]]
    return node



def makeGrid():
    for j in range(14):
        for i in range(28):
            if j == 0 or j == 14 or i == 0 or i == 28:
                firstValue = random.randint(0,25)
                secondValue = random.randint(0,25)
                thirdValue = random.randint(0,25)
            else:
                if 10 < matrix[j-1][i-1][0] < 245:
                    firstValue = matrix[j-1][i-1][0]
                    '''+ random.randint(-10, 10)'''
                elif matrix[j-1][i-1][0] < 10:
                    firstValue = matrix[j-1][i-1][0]
                    '''+ random.randint(-matrix[j-1][i-1][0], 10)'''
                else:
                    firstValue = matrix[j-1][i-1][0]
                    '''+ random.randint(-10, 255-matrix[j-1][i-1][0])'''

                if 10 < matrix[j-1][i-1][1] < 245:
                    secondValue = matrix[j-1][i-1][1]
                    '''+ random.randint(-10, 10)'''
                elif matrix[j-1][i-1][1] < 10:
                    secondValue = matrix[j-1][i-1][1]
                    '''+ random.randint(-matrix[j-1][i-1][1], 10)'''
                else:
                    secondValue = matrix[j-1][i-1][1]
                    ''''+ random.randint(-10, 255-matrix[j-1][i-1][1])'''

                if 10 < matrix[j-1][i-1][2] < 245:
                    thirdValue = matrix[j-1][i-1][2]
                    '''+ random.randint(-10, 10)'''
                elif matrix[j-1][i-1][2] < 10:
                    thirdValue = matrix[j-1][i-1][2]
                    '''+ random.randint(-matrix[j-1][i-1][2], 10)'''
                else:
                    thirdValue = matrix[j-1][i-1][2]
                    '''+ random.randint(-10, 255-matrix[j-1][i-1][2])'''
            matrix[j][i] = [firstValue, secondValue, thirdValue]


makeGrid()


def updateGrid():
    for j in range(14):
        for i in range(28):
            quadLoop = pyglet.graphics.vertex_list(4, ('v2i', (10 + (i * 50), 30 + (j*50), 50 + (i * 50), 30 + (j*50), 50 + (i * 50), 70 +(j*50), 10 + (i * 50), 70 +(j*50))), ('c3B', (colorChoice[0], colorChoice[1], colorChoice[2], colorChoice[0], colorChoice[1], colorChoice[2], matrix[j][i][0], matrix[j][i][1], matrix[j][i][2], matrix[j][i][0], matrix[j][i][1], matrix[j][i][2])))
            quadLoop.draw(pyglet.gl.GL_QUADS)


@window.event
def on_draw():
    window.clear()
    updateGrid()
    drawOutline(location[1],location[0])
    label.draw()
    keys.draw()



def drawOutline(y,x):
     pyglet.gl.glColor4f(255, 0, 0, 1.0)
     pyglet.gl.glLineWidth(2.3)
     pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (10 + (y*50), 30 + (x*50), 50 + (y*50), 30 + (x*50))))
     pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (10 + (y*50), 30 + (x*50), 10 + (y*50), 70 + (x*50))))
     pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (50 + (y*50), 30 + (x*50), 50 + (y*50), 70 + (x*50))))
     pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (50 + (y*50), 70 + (x*50), 10 + (y*50), 70 + (x*50))))

startCounter = [0,1]
endCounter = [0,1]
startLoc = [1,1]
endLoc = [1,1]


@window.event
def on_key_press(symbol, modifiers):

    if symbol == key.A:
        matrix[7][14] = [255, 0, 0]
        #music.play()
    elif symbol == key.LEFT:
        if location[1] > 0:
            location[1] -= 1
    elif symbol == key.RIGHT:
        if location[1] < 27:
            location[1] += 1
    elif symbol == key.UP:
        if location[0] < 13:
            location[0] += 1
    elif symbol == key.DOWN:
        if location[0] > 0:
            location[0] -= 1
    elif symbol == key.R:
        makeGrid()
        counter[0] = 0
        startCounter[0] = 0
        endCounter[0] = 0
        for i in range(14):
            for j in range(28):
                values[i][j] = [-1, -1]

        location[0] = 7
        location[1] = 13
        counter[0] = 5
        counter[1] = 2
        priorStart[0] = 50
        priorStart[1] = 0
        priorEnd[0] = 50
        priorEnd[1] = 1
    elif symbol == key.S:
        if startCounter[0] == 0:
            matrix[location[0]][location[1]] = [0, 255, 0]
            values[location[0]][location[1]] = [-2,-2]
            startCounter[0] +=1
            startLoc[0] = location[0]
            startLoc[1] = location[1]


    elif symbol == key.E:
        if endCounter[0] == 0:
            matrix[location[0]][location[1]] = [255, 0, 0]
            endCounter[0] +=1
            endLoc[0] = location[0]
            endLoc[1] = location[1]
    elif symbol == key.ENTER:
        if endCounter[0] == 1 and startCounter[0] == 1:
            findPath(startLoc[0], startLoc[1])
    elif symbol == key.SPACE:
        replace = matrix[location[0]][location[1]]
        newColor = [255-replace[0], 255-replace[1], 255-replace[2]]
        if matrix[location[0]][location[1]][0] == 255 and matrix[location[0]][location[1]][1] == 0:
            endCounter[0]-= 1
            matrix[location[0]][location[1]] = [10,15,5]
        elif matrix[location[0]][location[1]][0] == 0 and matrix[location[0]][location[1]][1] == 255:
            startCounter[0]-= 1
            matrix[location[0]][location[1]] = [10, 15, 5]
        else:
            matrix[location[0]][location[1]] = newColor
            if newColor[0] > 150:
                values[location[0]][location[1]][0] = -2
                values[location[0]][location[1]][1] = -2
                print(values[location[1]][location[0]])

            else:
                print('1. ' + str(location[0]) + '  2.  ' + str(location[1]))
                print(values[location[0][location[1]]][0])
                values[location[0]][location[1]][0] = -1
                values[location[0]][location[1]][1] = -1



pyglet.app.run()
