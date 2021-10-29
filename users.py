import json
import os
from common import face_client
from lib.face import get_faces
import logging

logger = logging.getLogger('__name__')
USERS_FILE = os.getenv('USERS_FILE', 'users.json')

class Users:
    def __init__(self):
        self.face_id_set = set()
        self.users = self.reload()
        

    def reload(self):
        with open(USERS_FILE) as json_file:
            self.users = json.load(json_file)
        
        self.face_id_set = set([user['face_id'] for user in self.users if user.get('face_id')])

    
    def save(self):
        with open(USERS_FILE, 'w') as json_file:
            json.dump(self.users, json_file)
    
    def register(self):
        self.reload()
        for user in self.users:
            photo = user.get('photo')
            name = user.get('name')

            if not photo or not name:
                continue
            
            with open(photo, 'rb') as photo_file:
                faces = get_faces(photo_file)

                if len(faces) != 1:
                    logger.error(f'the number of faces in {photo} is not 1. Failed to register user "{name}"!')
                    continue
                
                user['face_id'] = faces[0].face_id
        
        self.save()
    
    def indentify_faces(self, faces):
        known = []
        unknown = []

        for face in faces:
            group = unknown
            if face.face_id in self.face_id_set:
                group = known
            group.append(face)
        
        return known, unknown
            



users = Users()



