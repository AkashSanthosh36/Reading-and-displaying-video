#Reading the input program

#importing required packages
import cv2

#creating a videocaptureobject
cap=cv2.VideoCapture(0)	#0 for live feed.if there are more cameras and u have to access the second pass 1

#checking if camera opened successfully
if(cap.isOpened()==False):
	print("Unable To Read Camera Feed")

#defining the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#creating a codec and videowriterobject
out=cv2.VideoWriter('video6.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

while(cap.isOpened()):
	#capturirng frame by frame
	ret,frame=cap.read()
	if(ret==True):
		out.write(frame)
		#displaying the resulting frame
		cv2.imshow('Frame',frame)

		#press 'q' on keyboard to exit
		if(cv2.waitKey(25) & 0XFF==ord('q')): #waitKey(25) means 25ms each frame will be displayed
			break
# When everything done, release the video capture object
cap.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()
