import cv2
import numpy as np
import dlib
import time
import tkinter
from tkinter import messagebox

def bakisYonu(lengthVertical,RlengthVertical):
    if lengthVertical/RlengthVertical>1.05:
        return 0 #Left
    elif RlengthVertical/lengthVertical>1.05:
        return 1 #right


def görselleştir():
    
        landmarks = predictor(gray, face)
      
        leftPoint= (landmarks.part(36).x,landmarks.part(36).y)
        rightPoint = (landmarks.part(39).x,landmarks.part(39).y)
        left2Point= (landmarks.part(37).x,landmarks.part(37).y)
        left3Point= (landmarks.part(41).x,landmarks.part(41).y)
        right2Point = (landmarks.part(38).x,landmarks.part(38).y)
        right3Point = (landmarks.part(40).x,landmarks.part(40).y)
        
        RleftPoint= (landmarks.part(42).x,landmarks.part(42).y)
        RrightPoint = (landmarks.part(45).x,landmarks.part(45).y)
        Rleft2Point= (landmarks.part(43).x,landmarks.part(43).y)
        Rleft3Point= (landmarks.part(47).x,landmarks.part(47).y)
        Rright2Point = (landmarks.part(44).x,landmarks.part(44).y)
        Rright3Point = (landmarks.part(46).x,landmarks.part(46).y)
        
        RtopLine1 = cv2.line(frame,RleftPoint,Rleft2Point,(0,255,0),1)
        RtopLine2 = cv2.line(frame,Rleft2Point,Rright2Point,(0,255,0),1)
        RtopLine3 = cv2.line(frame,Rright2Point,RrightPoint,(0,255,0),1)
        
        
        topLine1 = cv2.line(frame,leftPoint,left2Point,(0,255,0),1)
        topLine2 = cv2.line(frame,left2Point,right2Point,(0,255,0),1)
        topLine3 = cv2.line(frame,right2Point,rightPoint,(0,255,0),1)
        
        RbotLine1 = cv2.line(frame,RleftPoint,Rleft3Point,(0,255,0),1)
        RbotLine2 = cv2.line(frame,Rleft3Point,Rright3Point,(0,255,0),1)
        RbotLine3 = cv2.line(frame,Rright3Point,RrightPoint,(0,255,0),1)
        
        
        botLine1 = cv2.line(frame,leftPoint,left3Point,(0,255,0),1)
        botLine2 = cv2.line(frame,left3Point,right3Point,(0,255,0),1)
        botLine3 = cv2.line(frame,right3Point,rightPoint,(0,255,0),1)
        
        RhorizontalLine = cv2.line(frame,RleftPoint,RrightPoint,(0,0,255),1)
        #RverticalLine = cv2.line(frame,Rleft2Point,Rleft3Point,(0,0,255),1)
        
        
        horizontalLine = cv2.line(frame,leftPoint,rightPoint,(0,0,255),1)
        #verticalLine = cv2.line(frame,left2Point,left3Point,(0,0,255),1)
        
        lengthVertical = (landmarks.part(41).y + landmarks.part(40).y )/2 - (landmarks.part(37).y+landmarks.part(38).y)/2
        lengthHorizontal = landmarks.part(39).x - landmarks.part(36).x 
        RlengthVertical = (landmarks.part(47).y + landmarks.part(46).y )/2 - (landmarks.part(43).y+landmarks.part(44).y)/2
        RlengthHorizontal = landmarks.part(45).x - landmarks.part(42).x 
        
        return RlengthVertical , lengthVertical


predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture(0)

numBlink=0
lengthLast = 1
RlengthLast = 1
idx = 0
idxR=0
idxL=0
strx=""
stry=""
time1 = time.perf_counter()
time2 = 0

while True:
    
    
    inF=open("blinktext1.txt","r")
    data=inF.read()
    inF.close()
    
    
    if(data =="exit\n"):
        break
    
    else:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        time2 = time.perf_counter()
        faces = detector(gray)
        for face in faces:
            
            ################# Göz kırpma algılama
            görselleştir()
            
            RlengthNow,lengthNow =görselleştir()
            
            if lengthLast/lengthNow >=1.4 and RlengthLast/RlengthNow >=1.4 :
                outF = open("blinktext.txt", "w")    
                print("Blink{}".format(numBlink))
                print ("Blink{}".format(numBlink),file=outF)
                outF.close()
                numBlink+=1
                time1 = time.perf_counter()
                
            RlengthLast,lengthLast =görselleştir()
            
            ################## kafa konumuna göre bakış yönü
            RlengthVertical , lengthVertical = görselleştir()
            
            if idx<15:
                if bakisYonu(lengthVertical, RlengthVertical)==0:
                    idxL+=1
                elif bakisYonu(lengthVertical, RlengthVertical)==1:
                    idxR+=1
                idx+=1
                
            if idx>=15:
                
                if idxR>idxL:
                    stry="Right"
                    if stry!=strx:
                        print("Looking Right")
                    strx="Right"
                elif idxR<idxL:
                    stry="Left"
                    if stry!=strx:
                        print("Looking Left")
                    strx="Left"
                
                idx=0
                idxR = 0
                idxL = 0
         ##################3
            
            
        ################## kameradan alınan görüntüyü görsellleştirme  
        #cv2.imshow("Frame" , frame)

        key = cv2.waitKey(1)
        if key == 27:#esc ile çıkış
            break

    
        
    


'''
    if time2-time1>15:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("Uyarı", "Göz kırpın!")
        time2= time.perf_counter()
        time1= time.perf_counter()
        '''
       
outF = open("blinktext.txt", "w")         
print ("",file=outF)
outF.close()
inF = open("blinktext1.txt", "w")         
print ("",file=outF)
inF.close()
cap.release()
cv2.destroyAllWindows()

