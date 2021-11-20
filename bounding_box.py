import time
import os
import io
from azure_api import face_client, computervision_client
from users import users
import logging
import firebase
import json

logger = logging.getLogger('__name__')

ENV = os.getenv('ENV', 'dev')
limit_period = {
    'dev': 3,
    'prod': 1,
}[ENV]


class BoundingBox:
    def __init__(self, color=(255, 0, 0), position=((0, 0), (100, 100)), thickness=2, label=''):
        self.color = color
        self.position = position
        self.thickness = thickness
        self.label = label


face_last_call = time.time()
face_boxes = []

obj_last_call = time.time()
obj_boxes = []

people = []
packages = 0

def update_face_boxes(img):
    global face_last_call

    now = time.time()
    if now - face_last_call < limit_period:
        return

    face_last_call = now
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
            box.label = 'stranger'
            for user in users.users:
                if face_client.face.verify_face_to_face(face.face_id, user['face_id']).is_identical:
                    box.label = user['name']
                    box.color = (0, 255, 0)
                    break

            face_boxes.append(box)
        
        new_people = [{'name': face_box.label} for face_box in face_boxes]

        global people

        if new_people != people:
            people = new_people
            data = json.dumps(people)
            firebase.update_db('people', data)
    
    finally:
        return


def update_obj_boxes(img):
    global obj_last_call

    now = time.time()
    if now - obj_last_call < limit_period:
        return

    obj_last_call = now
    global obj_boxes
    
    try:
        objs = computervision_client.detect_objects_in_stream(io.BytesIO(img))
        obj_boxes = []
        for obj in objs.objects:
            if obj.confidence < 0.5 or obj.object_property not in ('Box', 'Office supplies'):
                continue
            
            box = BoundingBox()
            box.color = (255, 0, 0)
            obj_rectangle = obj.rectangle
            left, top = obj_rectangle.x, obj_rectangle.y
            right, bottom = obj_rectangle.x + obj_rectangle.w, obj_rectangle.y + obj_rectangle.h
            box.position = ((left, top), (right, bottom))
            box.label = 'package'

            obj_boxes.append(box)
        
        new_packages = len(obj_boxes)

        global packages

        if new_packages != packages:
            packages = new_packages
            data = packages
            firebase.update_db('packages', data)
    
    finally:
        return