import os
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

FACE_ENDPOINT = os.getenv('FACE_ENDPOINT', '')
FACE_KEY = os.getenv('FACE_KEY', '')
CV_ENDPOINT = os.getenv('CV_ENDPOINT', '')
CV_KEY = os.getenv('CV_KEY', '')

face_client = FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(FACE_KEY))
computervision_client = ComputerVisionClient(CV_ENDPOINT, CognitiveServicesCredentials(CV_KEY))