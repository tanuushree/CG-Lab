from OpenGL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import math
tx=0
ty=0
x1new = x2new = x3new = y1new = y2new = y3new = 0
sx=sy=0
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-500, 500, -500, 500)

def draw1(x1,y1,x2,y2,x3,y3):
    triangle(x1,y1,x2,y2,x3,y3)
    translation(x1,y1,x2,y2,x3,y3)

def draw2(x1,y1,x2,y2,x3,y3):
    global x1new,x2new,x3new,y1new,y2new,y3new
    triangle(x1,y1,x2,y2,x3,y3)
    rotation(x1new,y1new,x2new,y2new,x3new,y3new)


def draw3(x1,y1,x2,y2,x3,y3):
    global sx,sy
    triangle(x1,y1,x2,y2,x3,y3)
    scaling(sx*x1,sy*y1,sx*x2,sy*y2,sx*x3,sy*y3)

def draw4(x1,y1,x2,y2,x3,y3,c):
    triangle(x1,y1,x2,y2,x3,y3)
    if c==1:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,-y1)
        glVertex2f(x2,-y2)
        glVertex2f(x3,-y3)
        glEnd()
        glFlush()
    elif c==2:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,y1)
        glVertex2f(-x2,y2)
        glVertex2f(-x3,y3)
        glEnd()
        glFlush()
    elif c==3:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
        glFlush()
    elif c==4:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(y1,x1)
        glVertex2f(y2,x2)
        glVertex2f(y3,x3)
        glEnd()
        glFlush()
    elif c==5:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
        glFlush()
    

def triangle(x1,y1,x2,y2,x3,y3):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    #glutSwapBuffers()
    glFlush()


def translation(x1,y1,x2,y2,x3,y3):
    global tx,ty
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+tx,y1+ty)
    glVertex2f(x2+tx,y2+ty)
    glVertex2f(x3+tx,y3+ty)
    glEnd()
    #glutSwapBuffers()
    glFlush()

def rotation(x1,y1,x2,y2,x3,y3):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    #glutSwapBuffers()
    glFlush()

def scaling(x1,y1,x2,y2,x3,y3):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    #glutSwapBuffers()
    glFlush()



def main():
    global tx,ty
    global x1new,x2new,x3new,y1new,y2new,y3new,sx,sy
    print("Enter coordinates of the triangle :")
    x1=float(input("x1= "))
    y1=float(input("y1= "))
    x2=float(input("x2= "))
    y2=float(input("y2= "))
    x3=float(input("x3= "))
    y3=float(input("y3= "))
	
	for i in range 5:
		n=float(input("\n1.translation\n2.rotation\n3.scaling\n4.reflection\nSelect an option : "))
		if (n==1):
		    tx=int(input("Enter tx : "))
		    ty=int(input("Enter ty : "))
		    glutInit()
		    glutInitDisplayMode(GLUT_RGBA)
		    glutInitWindowSize(1000,1000)
		    glutInitWindowPosition(0,0)
		    glutCreateWindow("translation")
		    glutDisplayFunc(lambda: draw1(x1,y1,x2,y2,x3,y3))
		    init()
		    glutMainLoop()

		elif (n==2):
		    theta=float(input("Enter a theta : "))
		    radian=theta*math.pi/180
		    x1new=x1*math.cos(radian)-y1*math.sin(radian)
		    x2new=x2*math.cos(radian)-y2*math.sin(radian)
		    x3new=x3*math.cos(radian)-y3*math.sin(radian)
		    y1new=x1*math.sin(radian)+y1*math.cos(radian)
		    y2new=x2*math.sin(radian)+y2*math.cos(radian)
		    y3new=x3*math.sin(radian)+y3*math.cos(radian)
		    glutInit()
		    glutInitDisplayMode(GLUT_RGBA)
		    glutInitWindowSize(1000,1000)
		    glutInitWindowPosition(0,0)
		    glutCreateWindow("rotation")
		    glutDisplayFunc(lambda: draw2(x1,y1,x2,y2,x3,y3))
		    init()
		    glutMainLoop()
		
		elif(n==3):
		    sx=float(input("enter sx = "))
		    sy=float(input("enter sy = "))
		    glutInit()
		    glutInitDisplayMode(GLUT_RGBA)
		    glutInitWindowSize(1000,1000)
		    glutInitWindowPosition(0,0)
		    glutCreateWindow("scaling")
		    glutDisplayFunc(lambda: draw3(x1,y1,x2,y2,x3,y3))
		    init()
		    glutMainLoop()


		elif (n==4):
		    c = int(input("\nreflection about \n1.x axis\n2.y axis\n3.origin\n4.x=y\n5.x=-y\nSelect an operation : "))
		    glutInit()
		    glutInitDisplayMode(GLUT_RGBA)
		    glutInitWindowSize(1000,1000)
		    glutInitWindowPosition(0,0)
		    glutCreateWindow("scaling")
		    glutDisplayFunc(lambda: draw4(x1,y1,x2,y2,x3,y3,c))
		    init()
		    glutMainLoop()

     


        
        


    
if __name__=="__main__":
    main()
