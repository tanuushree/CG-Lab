from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

x_min, y_min = 50, 50
x_max, y_max = 200, 200

x1, y1 = 30, 120
x2, y2 = 150, 10

def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

def cohen_sutherland(value):
    global x1, y1, x2, y2

    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x, y = 0, 0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = int(x), int(y)
                code1 = compute_code(x1, y1)

            else:
                x2, y2 = int(x), int(y)
                code2 = compute_code(x2, y2)

    if accept:
        draw_clipped_line()

def draw_actual_line():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_clipped_line():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_clipping_window():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min)
    glVertex2f(x_min, y_max)
    glVertex2f(x_max, y_max)
    glVertex2f(x_max, y_min)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_clipping_window()
    draw_actual_line()
    glutSwapBuffers()
    time.sleep(5)
    cohen_sutherland(0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutCreateWindow(b"Cohen-Sutherland Line Clipping")

gluOrtho2D(0, 300, 0, 300)

glutDisplayFunc(display)

glClearColor(0.0, 0.0, 0.0, 1.0)

glutMainLoop()
