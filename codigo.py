"""Cannon con mayor velocidad y blancos que reaparecen."""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Dispara hacia la posición del clic."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 12.5
        speed.y = (y + 200) / 12.5


def inside(xy):
    """Comprueba si una posición está dentro de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja el proyectil y los blancos."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Mueve los objetos y reposiciona los blancos que salen."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        targets.append(vector(200, y))

    for target in targets:
        target.x -= 1.0

        # Si sale por la izquierda, reaparece por la derecha.
        if target.x <= -200:
            target.x = 199
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Elimina los blancos alcanzados por el proyectil.
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if not inside(ball) or abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Siempre programa la siguiente actualización.
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)

move()
done()