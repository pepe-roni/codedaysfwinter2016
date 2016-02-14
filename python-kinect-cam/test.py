from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import freenect
import calib
import numpy as np
import cv
import threading
import openni
#GLOBALS#
IMGWIDTH   = 640
IMGHEIGHT = 480
#global hsv are set by sliders
hue = 80 #default hue for slider
sat = 10 #default saturation for slider
val = 50
rotate = 0.1
#global cv images
imgHsv = cv.CreateImage((IMGWIDTH, IMGHEIGHT), 8, 3)
imgHue = cv.CreateImage((IMGWIDTH, IMGHEIGHT), 8, 1)
imgSat = cv.CreateImage((IMGWIDTH, IMGHEIGHT), 8, 1)
imgVal = cv.CreateImage((IMGWIDTH, IMGHEIGHT), 8, 1)
imgBin = cv.CreateImage((IMGWIDTH, IMGHEIGHT), 8, 1)
imgOut = cv.CreateMat(IMGHEIGHT,IMGWIDTH, cv.CV_8UC3)

# the callback on the trackbar

def on_hueTrackbar(value):
    global hue
    hue = value

def on_satTrackbar(value):
    global sat
    sat = value

def on_valTrackbar(value):
    global val
    val = value

def cvProcess ():
        #set up opencv windows
    cv.NamedWindow("Camera", 1)
    cv.NamedWindow("Binary", 1)
    cv.NamedWindow("Settings", 1)

        #set up sliders
    cv.CreateTrackbar("Hue", "Settings", hue, 180, on_hueTrackbar)
    cv.CreateTrackbar("Sat", "Settings", sat, 255, on_satTrackbar)
    cv.CreateTrackbar("Val", "Settings", val, 255, on_valTrackbar)

    #run a blocking while loop to capture depth and rgb to opencv window
    while 1:

            #pull in camera data
        (depth,_),(rgb,_)=freenect.sync_get_depth(),freenect.sync_get_video()
        depth=depth.astype(np.uint8)

        h1, w1 = depth.shape[:2]
        h2, w2 = rgb.shape[:2]
        maxHeight= max(h1,h2)
        vis = np.zeros((maxHeight, w1+w2), np.uint8)
        vis2 = np.zeros((h2,w2), np.uint8)
        cv.CvtColor(rgb, vis2, cv.CV_BGR2GRAY)

            #display in a single window
        vis[:maxHeight, :w1] = depth
        vis[:maxHeight, w1:w1+w2] = vis2
        cv.ShowImage("Camera",vis)
        cv.WaitKey(100)

class OpenCVThread ( threading.Thread ):
    """OpenCVThread runs the opencv specific windowing functions in a non
       blocking way so that it can be interleaved with the GLUT windowing
       calls"""

    def run ( self ):
        #set up opencv windows
        cv.NamedWindow("Camera", 1)
        cv.NamedWindow("Binary", 1)
        cv.NamedWindow("Settings", 1)

        #set up sliders
        cv.CreateTrackbar("Hue", "Settings", hue, 180, on_hueTrackbar)
        cv.CreateTrackbar("Sat", "Settings", sat, 255, on_satTrackbar)
        cv.CreateTrackbar("Val", "Settings", val, 255, on_valTrackbar)

        #run a blocking while loop to capture depth and rgb to opencv window
        while 1:
            #pull in camera data
            (depth,_),(rgb,_)=freenect.sync_get_depth(),freenect.sync_get_video()
            depth=depth.astype(np.uint8)

            h1, w1 = depth.shape[:2]
            h2, w2 = rgb.shape[:2]
            maxHeight= max(h1,h2)
            vis = np.zeros((maxHeight, w1+w2), np.uint8)
            vis2 = np.zeros((h2,w2), np.uint8)
            cv.CvtColor(cv.fromarray(rgb), cv.fromarray(vis2), cv.CV_BGR2GRAY)

            #display in a single window
            vis[:maxHeight, :w1] = depth
            vis[:maxHeight, w1:w1+w2] = vis2
            cv.ShowImage("Camera",cv.fromarray(vis))
            cv.WaitKey(100)
try:
    TEXTURE_TARGET = GL_TEXTURE_RECTANGLE
except:
    TEXTURE_TARGET = GL_TEXTURE_RECTANGLE_ARB
light_diffuse  = [1.0, 0.0, 0.0, 1.0]
light_position = [1.0, 1.0, 1.0, 0.0]


def create_texture():
    global rgbtex
    rgbtex = glGenTextures(1)
    glBindTexture(TEXTURE_TARGET, rgbtex)
    glTexImage2D(TEXTURE_TARGET,0,GL_RGB,IMGWIDTH,IMGHEIGHT,0,GL_RGB,GL_UNSIGNED_BYTE,None)

def update():
    global projpts, rgb, depth
    global hue,sat,val
    global imgHsv,imgHue,imgSat,imgVal
    range2=25.0
    depth,_ = freenect.sync_get_depth()
    rgb,_ = freenect.sync_get_video()
    #convert numpy to opencv image
    img = cv.fromarray(rgb)

    #MAIN IMAGE PROCESSING WORK IN OPENCV HERE
    cv.CvtColor(img, imgHsv, cv.CV_BGR2HSV)
    cv.Split(imgHsv, imgHue, imgSat, imgVal, None)
    cv.InRangeS(imgHue,(hue-range2, 0, 0),(hue+range2, 0, 0),imgHue)
    cv.InRangeS(imgSat,(sat, 0, 0),(255, 0, 0),imgSat)
    cv.InRangeS(imgVal,(val, 0, 0),(255, 0, 0),imgVal)
    cv.And(imgHue,imgSat,imgBin)
    cv.And(imgBin,imgVal,imgBin)
    cv.Erode(imgBin,imgBin,None)
    cv.Dilate(imgBin,imgBin,None)
    cv.CvtColor(imgBin, imgOut, cv.CV_GRAY2BGR)
    cv.ShowImage("Binary",imgOut)
    #FINISH IMAGE PROCESSING
    #return to numpy array
    rgb = np.asarray(imgOut)
    q = depth.astype(np.uint16)
    X,Y = np.meshgrid(range(IMGWIDTH),range(IMGHEIGHT))
    d = 1
    projpts = calib.depth2xyzuv(q[::d,::d],X[::d,::d],Y[::d,::d])

def drawPointCloud():
    if not 'rgbtex' in globals():
        create_texture()

    rgb_ = (rgb.astype(np.float32) * 4 + 70).clip(0,255).astype(np.uint)
    glBindTexture(TEXTURE_TARGET, rgbtex)
    glTexSubImage2D(TEXTURE_TARGET, 0, 0, 0, IMGWIDTH, IMGHEIGHT, GL_RGB, GL_UNSIGNED_BYTE, rgb_)
    xyz, uv = projpts
    glMatrixMode(GL_TEXTURE)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glVertexPointerf(xyz)
    glTexCoordPointerf(uv)
    glPointSize(2)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glEnable(TEXTURE_TARGET)
    glColor3f(1,1,1)
    glDrawElementsui(GL_POINTS, np.array(range(xyz.shape[0])))
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisable(TEXTURE_TARGET)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    #drawBox()
    update()
    drawPointCloud()
    glutSwapBuffers()

def processNormalKeys(key, x, y):
    if key == "a":
        exit(0)

def processSpecialKeys(key, xx, yy):
    fraction = 0.1
    if key==100 :
        glRotatef(2, 0, 0, 1);

    elif key== 102 :
        glRotatef(-2, 0, 0, 1);
    if key==103 :
        glRotatef(2, 0, 1, 0);
    elif key== 101 :
        glRotatef(-2, 0, 1, 0);
def init():
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(  40.0,1.0,1.0,10.0)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowPosition(100,100);
glutInitWindowSize(IMGWIDTH,IMGHEIGHT);
glutCreateWindow("3d viewer")
glutKeyboardFunc(processNormalKeys)
glutSpecialFunc(processSpecialKeys)
glutMouseFunc(mouse)
glutDisplayFunc(display)
glutIdleFunc(display)
init()
OpenCVThread().start()
glutMainLoop()
glEnable(GL_DEPTH_TEST);