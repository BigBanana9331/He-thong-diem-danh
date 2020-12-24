import face_recognition
import cv2
import os
import pickle
import time
import db 
import numpy as np
from threading import Thread

myDB = db.connectDb()
cursor = myDB.cursor()


def gstreamer_pipeline(
    capture_width=3280,
    capture_height=2464,
    display_width=820,
    display_height=616,
    framerate=21,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

print(cv2.__version__)

fpsReport=0
scaleFactor=.25

Encodings=[]
Names=[]
process=True

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

timeStamp = time.time()
while True:
    _,frame=cam.read()
    frameSmall=cv2.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)
    frameRGB = frameSmall[:, :, ::-1]
    # frameRGB=cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB,model='cnn')
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)
    recogName = ""
    # if process:
    #     facePositions=face_recognition.face_locations(frameRGB,model='cnn')
    #     allEncodings=face_recognition.face_encodings(frameRGB,facePositions)
    for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
        name='Unkown Person'
        matches=face_recognition.compare_faces(Encodings,face_encoding)
        # if True in matches:
        #     first_match_index=matches.index(True)
        #     name=Names[first_match_index]
        face_distances = face_recognition.face_distance(Encodings,face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = Names[best_match_index]

        top=int(top/scaleFactor)
        right=int(right/scaleFactor)
        bottom=int(bottom/scaleFactor)
        left=int(left/scaleFactor)

        cv2.rectangle(frame,(left,top),(right, bottom),(0,0,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(0,0,255),2)
        print("Day la mat cua: ", name)
        recogName = name
    
    data = (1, recogName)
    db.updateStudentsStatus(myDB, cursor, data)
    dt=time.time()-timeStamp
    fps=1/dt
    fpsReport=.90*fpsReport + .1*fps
    print('fps is:',round(fpsReport,1))
    timeStamp=time.time()
    cv2.rectangle(frame,(0,0),(100,40),(0,0,255),-1)
    cv2.putText(frame,str(round(fpsReport,1))+ 'fps',(0,25),font,.75,(0,255,255,2))
    cv2.imshow('Picture',frame)
    cv2.moveWindow('Picture',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
