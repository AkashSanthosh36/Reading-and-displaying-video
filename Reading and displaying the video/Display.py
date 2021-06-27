import cv2
cap=cv2.VideoCapture('video6.avi')
while(cap.isOpened()):
	ret,frame=cap.read()
	if(ret==True):
		#displaying the resulting frame
		cv2.imshow('Frame',frame)
		cv2.waitKey(25)
	else:
		break	
cap.release()
cv2.destroyAllWindows()
