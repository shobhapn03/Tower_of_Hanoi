import turtle
import time  # Import time module to add delays

# Set up the screen
turtle.setup(780, 350)
turtle.hideturtle()
turtle.title("Tower of Hanoi - PythonTurtle.Academy")
turtle.speed(0)
turtle.tracer(0, 0)

# Initial settings
peg_height = 300
ring_height = 20
ring_width_max = 150
ring_delta_max = 30
animation_step = 5  # Reduce animation step for slower movement

A, B, C = [], [], []  # Pegs
T = []  # List of turtles for rings


def draw_line(x, y, heading, length, pensize, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.forward(length)


def draw_scene():
    turtle.bgcolor('light blue')
    draw_line(-600, -100, 0, 1200, 10, 'brown')
    for i in range(-250, 251, 250):
        draw_line(i, -93, 90, peg_height, 5, 'black')


def initialize(n):
    ring_delta = min(135 / (n - 1), ring_delta_max)
    for i in range(n):
        A.append(i)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor('red')
        t.fillcolor('light green')
        T.append(t)
    return ring_delta


def draw_single_ring(r, x, k, extra=0):
    w = ring_width_max - ring_delta * r
    T[r].up()
    T[r].goto(x - w / 2, -95 + ring_height * k + extra)
    T[r].down()
    T[r].setheading(0)
    T[r].begin_fill()
    for _ in range(2):
        T[r].forward(w)
        T[r].left(90)
        T[r].forward(ring_height)
        T[r].left(90)
    T[r].end_fill()


def draw_rings():
    for i in range(len(A)):
        draw_single_ring(A[i], -250, i)
    for i in range(len(B)):
        draw_single_ring(B[i], 0, i)
    for i in range(len(C)):
        draw_single_ring(C[i], 250, i)


def move_ring(PP, QQ):
    x = {"A": -250, "B": 0, "C": 250}[PP]
    x2 = {"A": -250, "B": 0, "C": 250}[QQ]
    P = {"A": A, "B": B, "C": C}[PP]
    Q = {"A": A, "B": B, "C": C}[QQ]

    for extra in range(1, 250 - (-95 + ring_height * (len(P) - 1)), animation_step):
        T[P[-1]].clear()
        draw_single_ring(P[-1], x, len(P) - 1, extra)
        turtle.update()
        time.sleep(0.01)  # Add a small delay

    T[P[-1]].clear()
    draw_single_ring(P[-1], x, len(P) - 1, extra)
    turtle.update()

    step = animation_step if x2 > x else -animation_step
    for tp in range(x, x2, step):
        T[P[-1]].clear()
        draw_single_ring(P[-1], tp, len(P) - 1, extra)
        turtle.update()
        time.sleep(0.01)  # Add a small delay
    T[P[-1]].clear()
    draw_single_ring(P[-1], x2, len(P) - 1, extra)
    turtle.update()

    Q.append(P.pop())
    for extra in range(250 - (-95 + ring_height * (len(Q) - 1)), 0, -animation_step):
        T[Q[-1]].clear()
        draw_single_ring(Q[-1], x2, len(Q) - 1, extra)
        turtle.update()
        time.sleep(0.01)  # Add a small delay
    T[Q[-1]].clear()
    draw_single_ring(Q[-1], x2, len(Q) - 1)
    turtle.update()


def tower_of_hanoi(X, Y, Z, n):
    if n == 1:
        move_ring(X, Z)
        return
    tower_of_hanoi(X, Z, Y, n - 1)
    move_ring(X, Z)
    tower_of_hanoi(Y, X, Z, n - 1)


draw_scene()
turtle.update()
n = int(turtle.numinput('Number of Rings', 'Please enter number of rings:', 5, 2, 10))
ring_delta = initialize(n)
draw_rings()
tower_of_hanoi("A", "B", "C", n)
turtle.update()
turtle.done()
