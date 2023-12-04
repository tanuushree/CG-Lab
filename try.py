from OpenGL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import math
r2 = 15
xc2,yc2 = 105,142
x4,y4 = 75,80
x5,y5 = 100,130
r4 = 15
xc4,yc4 = 395,142
x3,y3 = 425,80
x6,y6 = 400,130
point_visit =[(75,130),(83,130),(91,130),(100,130)]
current = 0
coordinate = list(point_visit[0])
speed = 1.0

#draw circle
def plot_points(xc,yc,x,y):
	glVertex2f(x+xc,y+yc)
	glVertex2f(y+xc,x+yc)
	glVertex2f(-x+xc,y+yc)
	glVertex2f(-y+xc,x+yc)
	glVertex2f(-x+xc,-y+yc)
	glVertex2f(-y+xc,-x+yc)
	glVertex2f(x+xc,-y+yc)
	glVertex2f(y+xc,-x+yc)
	
def draw_circle(r,xc,yc):
	x = 0
	y = r
	p=1-r
	glBegin(GL_POINTS)
	while x <= y:
		if p<0:
			p=p+2*x+1
		else:
			y-=1
			p=p-2*y+2*x+1
			
		plot_points(xc,yc,x,y)
		x+=1
	glEnd()
	glFlush()

def draw_line(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1
	steps = max(abs(dx),abs(dy))
	x_inc = dx/steps
	y_inc = dy/steps
	x,y=x1,y1
	glBegin(GL_POINTS)
	for i in range(steps+1):
		glVertex2f(x,y)
		x+=x_inc
		y+=y_inc
	glEnd()
	glFlush()


def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0.0,500.0,0.0,500.0)

def player1():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r1 = 20
	xc1,yc1 = 50,150
	draw_circle(r1,xc1,yc1)
	x1,y1 = 50,130
	x2,y2 = 50,30
	x3,y3 = 25,80
	x4,y4 = 75,80
	draw_line(x1,y1,x2,y2)
	draw_line(x1,y1,x3,y3)
	draw_line(x1,y1,x4,y4)

def player2():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r3 = 20
	xc3,yc3 = 450,150
	draw_circle(r3,xc3,yc3)
	x1,y1 = 450,130
	x2,y2 = 450,30
	x3,y3 = 425,80
	x4,y4 = 475,80
	x5,y5 = 400,130
	draw_line(x1,y1,x2,y2)
	draw_line(x1,y1,x3,y3)
	draw_line(x1,y1,x4,y4)

def rac1():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r2 = 15
	xc2,yc2 = 105,142
	draw_circle(r2,xc2,yc2)
	x4,y4 = 75,80
	x5,y5 = 100,130
	draw_line(x4,y4,x5,y5)

def rac2():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r4 = 15
	xc4,yc4 = 395,142
	draw_circle(r4,xc4,yc4)
	x3,y3 = 425,80
	x5,y5 = 400,130
	draw_line(x3,y3,x5,y5)

def ball():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r5 = 10
	xc5,yc5 = 200,142
	draw_circle(r5,xc5,yc5)

def showscreen():
	player1()
	player2()
	rac1()
	glutSwapBuffers()
	rac2()
	ball()

def animate1(temp):
	global coordinate,current
	tx,ty=point_visit[current]
	coord = [75,83.3,91.6,100]
	if (x5<101):
		x5+=8.3
	else:
		x5 = 100
	
	glutPostRedisplay()
	glutTimerFunc(100,animate1,0)		

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Two people playing tennis")
	init()
	glutDisplayFunc(showscreen)
	glutIdleFunc(showscreen)
	
	glutMainLoop()

if __name__ == "__main__":
	main()
