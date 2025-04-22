import cv2

face_cap= cv2.CascadeClassifier("")
video_cap=cv2.VideoCapture(0)
while True:
    ret, video_data=video_cap.read()
    col= cv2.cvtColor(video_data.cv2.COLOR_BGR2GRAY)
    faces=face_cap,detectMultiScale(
         col,
         scaleFactor=1.1,
         minNeighbour=5,
         minSize=(30,30),
         flag=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
         cv2.rectangle(video_data,(x,y),(x+w,x+h),(0,255,0),2)





    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
         break
video_cap.realese


















                                                             #  Jay Kumar Singh
