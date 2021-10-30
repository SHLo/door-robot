import json
import os
from azure_api import face_client
import logging

logger = logging.getLogger('__name__')
USERS_FILE = os.getenv('USERS_FILE', 'users.json')

class Users:
    def __init__(self):
        self.face_id_map = {}
        self.users = []
        self.reload()
        

    def reload(self):
        with open(USERS_FILE) as json_file:
            self.users = json.load(json_file)
        
        self.face_id_map = {user['face_id']: user for user in self.users if user.get('face_id')}

    
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
                faces = face_client.face.detect_with_stream(photo_file)

                if len(faces) != 1:
                    logger.error(f'the number of faces in {photo} is not 1. Failed to register user "{name}"!')
                    continue
                
                user['face_id'] = faces[0].face_id
        
        self.save()

users = Users()



