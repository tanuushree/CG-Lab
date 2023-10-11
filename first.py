from OpenGL import*
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def showscreen():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	glPointSize(5.0)	
	glBegin(GL_POINTS)
	glVertex2f(0.0,0.1)
	glVertex2f(0.0,0.6)
	glEnd()
	glFlush()
	
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutCreateWindow("New Window")
glutDisplayFunc(showscreen)
glutIdleFunc(showscreen)
glutMainLoop()


