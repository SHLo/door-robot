# door-robot

A door robot who detects people and packages at your door 

## Installation

requirements for runtime environment

* python3.6 or higher
* opencv
* create one Face API and one Computer Vision on Azure Cognitive Service
* use envtemplate as template to create a .env file containing your Azure api configuration

```pip[3] install requirements.txt```

## User Registration

1. provide a clear photo for each user, can be placed in the photo folder
2. edit users.json to enter name and photo file path for each user, leave face_id as empty
3. when the program runs, it will firstly register all the users defined in user.json for further identification

## Robot Power On

```python[3] main.py poweron```

* when there are people at your door, the robot will recognize their faces and label them with bounding boxes
* when there is package at your door, the robot will recognize it and annotate it with a bounding boxe

