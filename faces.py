import time
import os
import io
from lib.face_api import face_client
from users import users
from bounding_box import BoundingBox

ENV = os.getenv('ENV', 'dev')
limit_period = {
    'dev': 3,
    'prod': 1,
}[ENV]

last_call = time.time()
face_boxes = []

def update_face_boxes(img):
    global last_call

    now = time.time()
    if now - last_call < limit_period:
        return

    last_call = now
    global face_boxes
    
    try:
        faces = face_client.face.detect_with_stream(io.BytesIO(img))
        face_boxes = []
        for face in faces:
            box = BoundingBox()
            box.color = (0, 0, 255)
            face_rectangle = face.face_rectangle
            left, top = face_rectangle.left, face_rectangle.top
            right, bottom = face_rectangle.left + face_rectangle.width, face_rectangle.top + face_rectangle.height
            box.position = ((left, top), (right, bottom))
            for user in users.users:
                if face_client.face.verify_face_to_face(face.face_id, user['face_id']).is_identical:
                    box.label = user['name']
                    box.color = (0, 255, 0)
                    break

            face_boxes.append(box)
    
    finally:
        return