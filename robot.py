
import cv2
import logging
import io
from users import users
import faces
from faces import update_face_boxes

logger = logging.getLogger('__name__')

class Robot:
    def __init__(self):
        pass

    def get_cap_img(self, cap):
        read_success, frame = cap.read()
        if not read_success:
            logger.error('failed to read capture')
            return
        
        encode_success, im_buf_arr = cv2.imencode('.jpg', frame)
        if not encode_success:
            logger.error('failed to encode image')
            return
        
        return frame, im_buf_arr


    def draw_bounding_boxes(self, frame, boxes):
        #print(boxes)
        for box in boxes:
            start, end = box.position
            cv2.rectangle(frame, start, end, box.color, box.thickness)
            x, y = start
            cv2.putText(frame, box.label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box.color, box.thickness)


    def power_on(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            frame, img = self.get_cap_img(cap)

            update_face_boxes(img)

            self.draw_bounding_boxes(frame, faces.face_boxes)

            cv2.imshow('robot vision', frame)
            
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

robot = Robot()