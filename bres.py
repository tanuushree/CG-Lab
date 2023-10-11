import sys
from OpenGL import*
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def draw_line(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1
	x,y=x1,y1
	p = 2*dy-dx
	glBegin(GL_POINTS)
	while(x<=x2):
		glVertex2f(x,y)
		x+=1
		if p<0:
			p=p+2*dy
		else:
			y+=1
			p=p+2*dy-2*dx
	glEnd()
	glFlush()

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0.0,500.0,0.0,500.0)

def showscreen():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	x1,y1 = 100,100
	x2,y2 = 400,400
	draw_line(x1,y1,x2,y2)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Line Drwaing using Bresenham")
	init()
	glutDisplayFunc(showscreen)
	glutIdleFunc(showscreen)
	glutMainLoop()

if __name__ == "__main__":
	main()


