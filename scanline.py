# Tanu Shree
#200221085 
#Scanline
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


width, height = 800, 600


polygon = [(100, 100), (300, 100), (300, 200), (100, 200)]

filled = False

def draw_polygon():
    if filled:
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        for vertex in polygon:
            glVertex2f(*vertex)
        glEnd()
    else:
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for vertex in polygon:
            glVertex2f(*vertex)
        glEnd()

def scan_line_fill():
    min_y = min(polygon, key=lambda p: p[1])[1]
    max_y = max(polygon, key=lambda p: p[1])[1]

    for y in range(min_y, max_y + 1):
        intersections = []

        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]

            if y1 > y2:
                x1, x2, y1, y2 = x2, x1, y2, y1

            if y1 <= y < y2:
                if y1 != y2:
                    x_intersection = int(x1 + (x2 - x1) * (y - y1) / (y2 - y1))
                else:
                    x_intersection = x1

                intersections.append(x_intersection)

        intersections.sort()
        for i in range(0, len(intersections), 2):
            x1, x2 = intersections[i], intersections[i + 1]
            glColor3f(0.0, 0.0, 1.0)  
            glBegin(GL_LINES)
            glVertex2i(x1, y)
            glVertex2i(x2, y)
            glEnd()
        glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_polygon()
    glFlush()
   
def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        scan_line_fill()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Scan Line Algorithm")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, width, 0, height)
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    glutMainLoop()
main()
