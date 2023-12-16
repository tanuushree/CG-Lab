from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initial positions of the players and the ball
player1_x, player1_y = -0.8, 0.0
player2_x, player2_y = 0.8, 0.0
ball_x, ball_y = 0.0, 0.0
ball_speed = 0.01
ball_direction = 1  # To change ball's direction

# Function to draw a circle
def draw_circle(radius, x, y):
    num_segments = 100
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(num_segments):
        angle = 2.0 * math.pi * i / num_segments
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

# Function to draw the stick figure player with a tennis racquet
def draw_player(x, y):
    glLineWidth(2.0)
    glColor3f(1.0, 1.0, 1.0)  # White color for stick figure
    draw_circle(0.05, x, y + 0.05)  # Head
    glBegin(GL_LINES)
    # Body
    glVertex2f(x, y)
    glVertex2f(x, y - 0.2)
    # Arms
    glVertex2f(x, y - 0.1)
    glVertex2f(x - 0.1, y - 0.15)  # Left arm
    glVertex2f(x, y - 0.1)
    glVertex2f(x + 0.1, y - 0.15)  # Right arm
    # Legs
    glVertex2f(x, y - 0.2)
    glVertex2f(x - 0.1, y - 0.3)  # Left leg
    glVertex2f(x, y - 0.2)
    glVertex2f(x + 0.1, y - 0.3)  # Right leg
    glEnd()
    # Racquet (Simple line and circle)
    if x > 0:  # If player is on the right side (player2)
        glBegin(GL_LINES)
        glVertex2f(x - 0.1, y - 0.15)
        glVertex2f(x - 0.2, y - 0.05)  # Racquet handle (line)
        glEnd()
        draw_circle(0.03, x - 0.2, y - 0.05)  # Racquet head (circle)
    else:  # If player is on the left side (player1)
        glBegin(GL_LINES)
        glVertex2f(x + 0.1, y - 0.15)
        glVertex2f(x + 0.2, y - 0.05)  # Racquet handle (line)
        glEnd()
        draw_circle(0.03, x + 0.2, y - 0.05)  # Racquet head (circle)

# Function to draw the tennis ball
def draw_ball(x, y):
    glColor3f(1.0, 0.0, 0.0)  # Red color for the ball
    draw_circle(0.02, x, y)  # Small red circle for the ball

# Function to update the animation
def update(value):
    global player1_x, player2_x, ball_x, ball_speed, ball_direction

    # Move players
    player1_x += 0.005
    player2_x -= 0.005

    # Move ball and handle ball collision with players
    ball_x += ball_speed * ball_direction
    if (player1_x - 0.15 <= ball_x <= player1_x + 0.15 and
        player1_y - 0.2 <= ball_y <= player1_y):
        ball_direction = 1  # Change ball's direction
    elif (player2_x - 0.15 <= ball_x <= player2_x + 0.15 and
          player2_y - 0.2 <= ball_y <= player2_y):
        ball_direction = -1  # Change ball's direction

    # If the ball reaches the edges, reset its position
    if ball_x >= 0.9 or ball_x <= -0.9:
        ball_x, ball_y = 0.0, 0.0

    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_player(player1_x, player1_y)
    draw_player(player2_x, player2_y)
    draw_ball(ball_x, ball_y)

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
