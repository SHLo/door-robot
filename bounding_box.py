class BoundingBox:
    def __init__(self, color=(255, 0, 0), position=((0, 0), (100, 100)), thickness=2, label='stranger'):
        self.color = color
        self.position = position
        self.thickness = thickness
        self.label = label