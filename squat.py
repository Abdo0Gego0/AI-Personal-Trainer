import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
     
detector = pm.poseDetector()
count = 0
dir = 0
pTime=0

while True:
                success,img = cap.read()
                img = cv2.resize(img,(1200,720))
                
                img = detector.findPose(img)
                lmList = detector.findPosition(img,False)
                #print(lmList)
                
                if len(lmList)!=0:
                        #pass
                        #right arm
                                #rightangle = detector.findAngle(img,12,14,16)
                        #left arm
                                angle  = detector.findAngle(img,24,26,28)
                                per = np.interp(angle,(210,310),(0,100))
                                bar = np.interp(angle,(220,310),(650,100))
                        
                                print(angle,per)
                        
                        #check for the dummble
                                if per == 100:
                                        if dir == 0:
                                                count+=0.5
                                                dir = 1
                                
                                if per == 0:
                                        if dir == 1:
                                                count+=0.25
                                                dir = 0
                                print(count)
                                
                                #draw bar
                                cv2.rectangle(img,(1100,100),(1000,650),(0,0,0),3)
                                cv2.rectangle(img,(1100,int(bar)),(1000,650),(255,255,255),cv2.FILLED)
                                cv2.putText(img,f'{int(per)}%',(1000,75),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
                                
                                # draw curl count
                                cv2.rectangle(img,(20,570),(160,720), (0,0,0),15)
                                cv2.rectangle(img,(20,580),(150,720),(255,255,255),cv2.FILLED)
                                cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)
                        
                                cTime = time.time()
                                fps = 1/(cTime-pTime)
                                pTime = cTime
                                cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)
                                
                                cv2.imshow('image',img)
                                cv2.waitKey(1)
                        
