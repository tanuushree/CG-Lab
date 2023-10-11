import sys
from OpenGL import*
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

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
	

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0.0,500.0,0.0,500.0)

def showscreen():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	r = 50
	xc,yc = 250,250
	draw_circle(r,xc,yc)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Circle Drawing using Midpoint")
	init()
	glutDisplayFunc(showscreen)
	glutIdleFunc(showscreen)
	glutMainLoop()

if __name__ == "__main__":
	main()

