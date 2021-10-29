
import cv2
from lib.face import get_faces

class Robot:
    def __init__(self):
        pass

    def power_on(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            known_faces, unknown_faces = 


            cv2.imshow('robot vision ',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

robot = Robot()