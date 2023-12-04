# Tanu Shree
#200221085 
#flood
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


window_size = 400
point_size = 4
sys.setrecursionlimit(100000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)



def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
  
    return pixel[0][0]


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def rectangle(vertices, color):
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


def plot_rect():
    glClear(GL_COLOR_BUFFER_BIT)
    
    gluOrtho2D(0, window_size, window_size, 0)
  
    rectangle(
        [[10, 10], [10, 100], [100, 100], [100, 10]],
        [1, 0.0, 0.0]
    )

    glFlush()


def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y, [0.0, 0.1, 1.0], get_pixel(x, y))


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(plot_rect)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()
