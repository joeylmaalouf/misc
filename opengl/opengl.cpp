// Included files
#include <GL/glut.h>


// Global variables
GLfloat xRotated, yRotated, zRotated;


void DrawCube(void)
{
	glMatrixMode(GL_MODELVIEW);
	// Clear the drawing buffer
	glClear(GL_COLOR_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0.0,0.0,-10.5);
	glRotatef(xRotated,1.0,0.0,0.0);
	glRotatef(yRotated,0.0,1.0,0.0);
	glRotatef(zRotated,0.0,0.0,1.0);
	glBegin(GL_QUADS);                // Draw The Cube Using quads
	glColor3f(0.0f,0.0f,1.0f);        // Color Blue
	glVertex3f( 1.0f, 1.0f,-1.0f);    // Top    Right Of The Quad (Top)
	glVertex3f(-1.0f, 1.0f,-1.0f);    // Top    Left  Of The Quad (Top)
	glVertex3f(-1.0f, 1.0f, 1.0f);    // Bottom Left  Of The Quad (Top)
	glVertex3f( 1.0f, 1.0f, 1.0f);    // Bottom Right Of The Quad (Top)
	glColor3f ( 1.0f, 0.5f, 0.0f);    // Color Orange
	glVertex3f( 1.0f,-1.0f, 1.0f);    // Top    Right Of The Quad (Bottom)
	glVertex3f(-1.0f,-1.0f, 1.0f);    // Top    Left  Of The Quad (Bottom)
	glVertex3f(-1.0f,-1.0f,-1.0f);    // Bottom Left  Of The Quad (Bottom)
	glVertex3f( 1.0f,-1.0f,-1.0f);    // Bottom Right Of The Quad (Bottom)
	glColor3f ( 1.0f, 0.0f, 0.0f);    // Color Red    
	glVertex3f( 1.0f, 1.0f, 1.0f);    // Top    Right Of The Quad (Front)
	glVertex3f(-1.0f, 1.0f, 1.0f);    // Top    Left  Of The Quad (Front)
	glVertex3f(-1.0f,-1.0f, 1.0f);    // Bottom Left  Of The Quad (Front)
	glVertex3f( 1.0f,-1.0f, 1.0f);    // Bottom Right Of The Quad (Front)
	glColor3f ( 1.0f, 1.0f, 0.0f);    // Color Yellow
	glVertex3f( 1.0f,-1.0f,-1.0f);    // Top    Right Of The Quad (Back)
	glVertex3f(-1.0f,-1.0f,-1.0f);    // Top    Left  Of The Quad (Back)
	glVertex3f(-1.0f, 1.0f,-1.0f);    // Bottom Left  Of The Quad (Back)
	glVertex3f( 1.0f, 1.0f,-1.0f);    // Bottom Right Of The Quad (Back)
	glColor3f ( 0.0f, 1.0f, 0.0f);    // Color Green
	glVertex3f(-1.0f, 1.0f, 1.0f);    // Top    Right Of The Quad (Left)
	glVertex3f(-1.0f, 1.0f,-1.0f);    // Top    Left  Of The Quad (Left)
	glVertex3f(-1.0f,-1.0f,-1.0f);    // Bottom Left  Of The Quad (Left)
	glVertex3f(-1.0f,-1.0f, 1.0f);    // Bottom Right Of The Quad (Left)
	glColor3f ( 1.0f, 0.0f, 1.0f);    // Color Violet
	glVertex3f( 1.0f, 1.0f,-1.0f);    // Top    Right Of The Quad (Right)
	glVertex3f( 1.0f, 1.0f, 1.0f);    // Top    Left  Of The Quad (Right)
	glVertex3f( 1.0f,-1.0f, 1.0f);    // Bottom Left  Of The Quad (Right)
	glVertex3f( 1.0f,-1.0f,-1.0f);    // Bottom Right Of The Quad (Right)
	glEnd();                          // End Drawing The Cube
	glCullFace(GL_BACK);
	glFlush();
}


void animation(void)
{
	// xRotated += 0.01;
	yRotated += 0.01;
	// zRotated += 0.01;
	DrawCube();
}


void reshape(int x, int y)
{
	if (x == 0 || y == 0) return;  // Nothing is visible then, so return
	
	// Set a new projection matrix
	glMatrixMode(GL_PROJECTION);  
	glLoadIdentity();
	
	// Angle of view: 50 degrees
	// Near clipping plane distance: 0.5
	// Far clipping plane distance: 20.0
	gluPerspective(50.0, (GLdouble)x/(GLdouble)y, 0.5, 20.0);
	
	glMatrixMode(GL_MODELVIEW);
	glViewport(0, 0, x, y);  // Use the whole window for rendering
}


int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glEnable(GL_LIGHTING);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	
	glClearColor(0, 0, 0, 0);
	glutDisplayFunc(DrawCube);
	glutReshapeFunc(reshape);
	
	// Set the function for the animation.
	glutIdleFunc(animation);
	// glutIdleFunc(DrawCube);
	
	glutMainLoop();
	return 0;
}
