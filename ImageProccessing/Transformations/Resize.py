import cv2
from . import TransformationInterface


class Resize(TransformationInterface):
    def __init__(self, size):
        self.size = size

    def apply(self, image):
        return cv2.resize(image, self.size)
