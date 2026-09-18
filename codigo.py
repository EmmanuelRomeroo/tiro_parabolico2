"""Cannon con proyectil y blancos más rápidos."""

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

        # Antes se dividía entre 25; ahora la velocidad es el doble.
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
    """Mueve el proyectil y los blancos."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        targets.append(vector(200, y))

    for target in targets:
        # Antes avanzaban 0.5 píxeles por actualización.
        target.x -= 1.0

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)

move()
done()
