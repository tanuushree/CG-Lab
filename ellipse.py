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


def draw_circle(a,b,xc,yc):
	x = 0
	y = b
	p= b**2 - (a**1 * b)+(0.25 * a**2)
	glBegin(GL_POINTS)
	while (2*(b**2)*x)<(2*(a**2)*y):
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(-x+xc,-y+yc)
		
		x+=1
		if p<0:
			p=p+2*b**2*x+b**2
		else:
			y-=1
			p=p+(2*b**2*x)-(2*a**2*y)+b**2
	p = b**2 * (x+0.5)**2 +a**2 * (y-1)**2 - (a**2 * b**2)
	while y>=0:
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(-x+xc,-y+yc)
		
		y-=1
		if p>0:
			p=p-(2*a**2 * y)+a**2
		else:
			x+=1
			p=p+(2* b** 2*x) - (2 * a**2 *y) +a**2
			
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
