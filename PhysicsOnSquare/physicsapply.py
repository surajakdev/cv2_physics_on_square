

import cv2
import mediapipe as mp
import time
import numpy as np
import time
import signal
from my_package.ThreadPage import CustomThread

class Impact():

  def __init__(self) -> None:
     
    mp_drawing=mp.solutions.drawing_utils
    mp_hands =mp.solutions.hands
    mp_drawing_styles = mp.solutions.drawing_styles

    # For static images:
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,min_detection_confidence=0.5)

    self.start:float = 0
    self.end:float = 0
    self.timeTaken:float=0
    self.tmass2:float=0
    self.flag=0
    self.flag1=0
    self.flag2=0
    self.image=None
    self.frcnt=0

    self.cap = cv2.VideoCapture(0)
  
    while self.cap.isOpened():
        
        self.m2=5 #kg
        self.m1=10 #kg
        self.s=2

        # reading camera frame.
        success, self.image = self.cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          continue
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # conversion bgr to rgb as mediapipe requires frames in bgr format to process image.
        results = hands.process(self.image)
        image_height, image_width, c = self.image.shape

        # orange line drawn.
        line = cv2.line(self.image, (0, 400), (700, 400), (255,127,0),3)

        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if self.flag==0:
        # red small box 1kg
          cv2.rectangle(self.image,(60,210),(40,190),(255, 0, 0),3)
        # blue big box
        cv2.rectangle(self.image,(50,220),(75,400),(0, 0, 255),3)

        line1 = cv2.line(self.image, (500, 200), (500, 450), (255,127,0),3)
        
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
          # for loop for drawing landmarks on hands
          for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                self.image,
                hand_landmarks,
                # for connecting differnt points in hand and draw landmarks.
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()),

            # x and y cordinate tuple from frames detected this tuple is of index fingers position.
            xcor = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            ycor= hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height

            if xcor<=500: 
              if self.start == 0:
                self.start=time.time()
                print("self.start:  ",self.start)

            if xcor<=60:
              if self.end == 0:
                self.end= time.time()
                
                self.timeTaken = self.end-self.start
                print("timeTaken",self.timeTaken)

            if self.timeTaken!=0 and self.tmass2==0:
              a= 2 * (500-60)/self.timeTaken**2
              self.tmass2=5*(300-85)/(10*a)
              print("tmass2 :",self.tmass2)

              self.flag=1
              self.flag2=1

        if self.flag2==1:
          print("self.flag2",self.flag2)
          print("check")
          thread = CustomThread(self)
          # start the thread
          thread.start()
          print("after start")
          self.flag2=0
        if self.flag1==1:
          cv2.rectangle(self.image,(40,400),(20,380),(0, 0, 255),3)

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(self.image, 1))
        # cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('r'):
          break
    self.cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    obj=Impact()












































# eeror message : from .import ThreadPage ImportError: attempted relative import with no known parent package

                
          #   print(f'Ring finger tip coordinates: (',
          #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
          # )



    #         for tuple_in_array in array_of_tuples:
    #           # for loop to check if the element with numerical value of coordinates detected tuple is within the numerical value range of line coordinates tuple.          
    #           if tuple_to_check[0] >= tuple_in_array[0] and tuple_to_check[1] <= tuple_in_array[1]:
    #             cv2.rectangle(image,(384,0),(510,128),(0,255,0),3)
    # # time is tame taken for m1 to move from one pixel point to other, watching it with pythons fn time and using formula ----> s=ut+half(at**2) --> u=0 so, a=2s/t**2
          
        ###################################   
            # t=time.time
            # 500-60 --> pixels mass1 travelled from left to right in screen
            # a= 2 * (500-60)/t**2 ----> 
            # tmass2=5*(300-85)/(10*a)
        ####################################    

            # if xcor<=500 and xcor>=70:
            #   start = time.time()