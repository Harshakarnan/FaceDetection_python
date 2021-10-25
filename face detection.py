import cv2
trainedfacemodel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
while True:

    workingcorrectly,frame=webcam.read()
    bandw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=trainedfacemodel.detectMultiScale(bandw)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,250,0),1)

    cv2.imshow('capture',frame)
    key=cv2.waitKey(1)
    if key==27:
        quite()
