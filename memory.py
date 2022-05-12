# Juego de memoria. Puzzle por pares de números

# Importar librerias
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward, left, end_fill
from turtle import clear, shape, stamp, write, update, ontimer, setup
from turtle import addshape, hideturtle, tracer, onscreenclick, done
from freegames import path

""" Declara variables como la imagen que se usará:
El contenido de los cuadros , estado y si estan o no ocultos."""
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

# Definición de las funciones


def square(x, y):
    """Dibuja cuadtros blancos con delinieado negro en (x, y)."""
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
    """Convierte coordenadas (x,y) a index de piezas"""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Devuelve una pieza a coordenadas (x,y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza la marca u oculta piezas segun sean presionados."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja imagen y piezas"""
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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


# Flujo principal
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()