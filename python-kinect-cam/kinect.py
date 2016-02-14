import freenect
import frame_convert
import cv2
import numpy as np
import imutils
from imutils.object_detection import non_max_suppression
from imutils import paths
from threading import Thread

detector = cv2.SimpleBlobDetector()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

#function to get depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array #freenect.sync_get_depth()

def get_people(frame):
    image = frame
    image = imutils.resize(image, width=min(800, image.shape[1]))
    faceCascade = cv2.CascadeClassifier("faces.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        image = image.copy()

    cv2.imshow('People detected picture', image)

while 1:
    #get a frame from RGB camera
    frame = get_video()
    #get a frame from depth sensor
    depth = get_depth()

    #display RGB image
    #Thread(target=get_people(frame)).start()
    #cv2.imshow('RGB image',frame)
    #display depth image
    cv2.imshow('Depth image', depth)

    # quit program when 'esc' key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()