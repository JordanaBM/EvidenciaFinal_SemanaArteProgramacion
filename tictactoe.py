"""Tic Tac Toe

Ejercicios

1. Dale a la X y a la O un color y ancho diferente.
2. ¿Qué pasa cuando alguien presiona una posición ocupada?
3. ¿Cómo detectarías cuando un jugador ha ganado?
4. ¿Cómo crearías un jugador que sea una computadora?
"""

import turtle

from freegames import line


def grid():
    """Dibuja la grilla tic-tac-toe."""
    turtle.pencolor("blue")
    turtle.bgcolor("white")
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja al jugador X."""
    turtle.pencolor("green")
    line(x+30, y+30, x + 100, y + 100)
    line(x+30, y + 100, x + 100, y+30)


def drawo(x, y):
    """Dibuja al jugador O."""
    turtle.pencolor("red")
    turtle.up()
    turtle.goto(x + 64, y + 20)
    turtle.down()
    turtle.circle(45)


def floor(value):
    """Redondea el valor al de la grilla."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
# Arreglo para verificar si un espacio ya está ocupado
places_on_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def draw_symbol(x, y, player):
    """Dibuja la X o la O correspondiente"""
    draw = players[player]
    draw(x, y)
    turtle.update()
    # Cambia de 'x' a 'o'
    state['player'] = not player


def tap(x, y):
    """Dibuja la X o la O en el cuadrado seleccionado."""
    global places_on_grid
    x = floor(x)
    y = floor(y)
    column = (x + 205)
    row = (-y + 205)
    square = column + row*3
    square = int(square)
    player = state['player']

    if square == 422:
        if places_on_grid[0] == " ":
            places_on_grid[0] = 1
            draw_symbol(x, y, player)

        elif places_on_grid[0] != "":
            print("Este espacio ya está ocupado")
    elif square == 555:
        if places_on_grid[1] == " ":
            places_on_grid[1] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")
    elif square == 688:
        if places_on_grid[2] == " ":
            places_on_grid[2] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")
    elif square == 821:
        if places_on_grid[3] == " ":
            places_on_grid[3] = 821
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")

    elif square == 954:
        if places_on_grid[4] == " ":
            places_on_grid[4] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")

    elif square == 1087:
        if places_on_grid[5] == " ":
            places_on_grid[5] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")

    elif square == 1220:
        if places_on_grid[6] == " ":
            places_on_grid[6] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")

    elif square == 1353:
        if places_on_grid[7] == " ":
            places_on_grid[7] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")

    elif square == 1486:
        if places_on_grid[8] == " ":
            places_on_grid[8] = 1
            draw_symbol(x, y, player)

        else:
            print("Este espacio ya está ocupado")


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
