from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
state2 = {'score': 0}

state3 = {'victoria': 0}


hide = [True] * 64
writer = Turtle(visible=False)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        state2['score'] += 1
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        state3['victoria'] += 1
        if state3['victoria']==31:
            up()
            goto(0, 0)
            color('Azul')
            write('Ganaste', align="center", font=('Arial', 500, 'normal'))




def draw():
    "Draw image and tiles."
    writer.undo()
    writer.write(state2['score'])


    clear()
    goto(0, 0)
    shape(car)
    stamp()



    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25, y)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))
        
        

    update()
    ontimer(draw, 100)




shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
writer.goto(300, 300)
writer.color('black')
writer.write(state2['score'])
draw()
done()
