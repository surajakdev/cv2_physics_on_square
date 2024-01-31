
import threading, time, subprocess
import cv2
from threading import Thread
 
# custom thread
class CustomThread(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.val = val
        self.rec1= None
        self.rec2=None
        self.rec3=None
        self.rec4=None
        self.flag1=self.val.flag1
        self.flag2=self.val.flag2

    def run(self):
        print("Its run")
        print("threads ***************",threading.active_count())

        # Time taken to reach 4 distinct points at some pixel heights(y-axis) , denoted as "t"
        t = (self.val.tmass2)/4

        if self.val.frcnt==0:
          for i in range(4):
              if i ==0:
                print("First")
                time.sleep(t)
                self.rec1 =cv2.rectangle(self.val.image,(40,220),(20,200),(255, 0, 0),3)
               
              elif i==1:
                print("second")
                time.sleep(t)              
                self.rec2 =cv2.rectangle(self.val.image,(40,280),(20,260),(255, 0, 0),3)
                
              elif i==2:
                print("third")              
                time.sleep(t)             
                self.rec3 =cv2.rectangle(self.val.image,(40,340),(20,320),(255, 0, 0),3)
                
              else:
                print("fourth")
                time.sleep(t)             
                self.rec4 =cv2.rectangle(self.val.image,(40,400),(20,380),(255, 0, 0),3)              
                self.val.flag1=1
                self.val.flag2=0
                print("###################")
                print("self.val.flag2",self.val.flag2)
















# ############################################### working #########################################
# import threading, time, subprocess
# import cv2
# import mediapipe as mp

# # SuperFastPython.com
# # example of returning multiple value from a thread
# from time import sleep
# from threading import Thread
 
# # custom thread
# class CustomThread(Thread):
#     # constructor
#     def __init__(self,val):
#         # execute the base constructor
#         Thread.__init__(self)
#         # set a default values
#         self.val = val

#         self.rec1= None
#         self.rec2=None
#         self.rec3=None
#         self.rec4=None
#         self.bool1=False
#         self.bool2=False
#         self.bool3=False
#         self.bool4=False
#         self.flag1=self.val.flag1
#         self.flag2=self.val.flag2
#         # self.c1
 
#     # function executed in a new thread
#     def run(self):
#         print("Its run")
#         print("threads ***************",threading.active_count())

#         if self.val.frcnt==0:
#           for i in range(4):
#               if i ==0:
#                 print("First")
#                 time.sleep(0.1)
#                 # self.bool1=True
#                 self.rec1 =cv2.rectangle(self.val.image,(40,220),(20,200),(255, 0, 0),3)
#                 # self.rec1=None

                
#               elif i==1:
#                 print("second")
#                 # self.bool2=True
#                 time.sleep(0.1)              
#                 self.rec2 =cv2.rectangle(self.val.image,(40,280),(20,260),(255, 0, 0),3)
                
#               elif i==2:
#                 print("third")              
#                 time.sleep(0.1)
#                 # self.bool3=True              
#                 self.rec3 =cv2.rectangle(self.val.image,(40,340),(20,320),(255, 0, 0),3)
                
#               else:
#                 print("fourth")
#                 time.sleep(0.1)
#                 # self.bool4=True              
#                 self.rec4 =cv2.rectangle(self.val.image,(40,400),(20,380),(255, 0, 0),3)              
#                 self.val.flag1=1
#                 self.val.flag2=0
#                 print("###################")
#                 print("self.val.flag2",self.val.flag2)

        # self.val.frcnt==1


































# # create a new thread
# thread = CustomThread()
# # start the thread
# thread.start()
# # wait for the thread to finish
# thread.join()
# report all values returned from a thread
# print(thread.value1)
# print(thread.value2)
# print(thread.value3)



# def tfn(image,parent):
#         for i in range(4):
#             if i ==0:
#               # time.sleep(1)
#               line =cv2.rectangle(image,(40,220),(20,200),(255, 0, 0),3)
#               return parent.flag1,parent.flag2,line
#             elif i==1:
#               # time.sleep(1)
#               cv2.rectangle(image,(40,280),(20,260),(255, 0, 0),3)
#             elif i==2:
#               # time.sleep(1)
#               cv2.rectangle(image,(40,340),(20,320),(255, 0, 0),3)
#             else:
#               # time.sleep(1)
#               cv2.rectangle(image,(40,400),(20,380),(255, 0, 0),3)
#               parent.flag1=3
#               parent.flag2=5