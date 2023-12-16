#Tanu Shree
#animate
#20221085
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

player1_y = 0.0
player2_y = 0.0
ball_x, ball_y = -0.8, 0.0
ball_speed = 0.01
ball_direction = 1

def draw_circle(radius, x, y):
    num_segments = 100
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(num_segments):
        angle = 2.0 * math.pi * i / num_segments
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

def draw_player(x, y):
    glLineWidth(2.0)
    glColor3f(1.0, 1.0, 1.0)

    draw_circle(0.05, x, y + 0.05)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y - 0.2)
    glVertex2f(x, y - 0.1)
    glVertex2f(x - 0.1, y - 0.15)  
    glVertex2f(x, y - 0.1)
    glVertex2f(x + 0.1, y - 0.15) 
    glVertex2f(x, y - 0.2)
    glVertex2f(x - 0.1, y - 0.3)  
    glVertex2f(x, y - 0.2)
    glVertex2f(x + 0.1, y - 0.3)  
    glEnd()

    glColor3f(1.0, 1.0, 1.0)

    if x > 0:
        glBegin(GL_LINES)
        glVertex2f(x - 0.1, y - 0.15)
        glVertex2f(x - 0.2, y - 0.05)  
        glEnd()
        draw_circle(0.03, x - 0.2, y - 0.05)  
    else:
        glBegin(GL_LINES)
        glVertex2f(x + 0.1, y - 0.15)
        glVertex2f(x + 0.2, y - 0.05)  
        glEnd()
        draw_circle(0.03, x + 0.2, y - 0.05)  

def draw_ball(x, y):
    glColor3f(1.0, 0.0, 0.0)  
    draw_circle(0.02, x, y)  

def update(value):
    global player1_y, player2_y, ball_x, ball_y, ball_speed, ball_direction

    ball_x += ball_speed * ball_direction

    if ball_x >= 0.8:
        ball_direction = -1

    elif ball_x <= -0.8:
        ball_direction = 1

    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_player(-0.8, player1_y)
    draw_player(0.8, player2_y)
    draw_ball(ball_x, 0.0)  

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Tennis Animation")

    glutDisplayFunc(display)
    glutTimerFunc(25, update, 0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)

    glutMainLoop()

if __name__ == "__main__":
    main()
