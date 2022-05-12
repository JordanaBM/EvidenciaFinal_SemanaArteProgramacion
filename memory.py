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
state = {'mark': None}
taps = 0
# Tamaño estandar para el puzzle=200
puzzle_size = 200
partition = 4
partsqr = partition*partition
tiles = list(range(partsqr//2)) * 2
hide = [True] * partsqr
sqr_size = puzzle_size*2//partition

# Definición de las funciones


def square(x, y):
    """Dibuja cuadtros blancos con delinieado negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(partition):
        forward(sqr_size)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x,y) a index de piezas"""
    return int((x + puzzle_size) // sqr_size +
               ((y + puzzle_size) // sqr_size) * partition)


def xy(count):
    """Devuelve una pieza a coordenadas (x,y)."""
    return ((count % partition) * sqr_size - puzzle_size,
            (count // partition) * sqr_size - puzzle_size)


def tap(x, y):
    """Actualiza la marca u oculta piezas segun sean presionados."""
    if(x > -puzzle_size and x < puzzle_size
       and y > -puzzle_size and y < puzzle_size):
        global taps
        taps = taps + 1
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

    for count in range(partsqr):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', int(
            180*(puzzle_size/200)/partition), 'normal'))
    up()
    tapCounter()
    update()
    ontimer(draw, 100)


def tapCounter():
    """Dibuja el contador de los taps"""
    global taps
    goto(-puzzle_size, -puzzle_size*1.2)
    color('black')
    write("Número de taps: "+str(taps), font=('Arial', 18, 'normal'))


# Flujo principal
shuffle(tiles)
setup(puzzle_size*2.2, puzzle_size*3, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
