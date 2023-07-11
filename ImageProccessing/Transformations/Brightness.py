import cv2
from . import TransformationInterface


class Brightness(TransformationInterface):
    def __init__(self, factor):
        self.factor = factor

    def apply(self, image):
        return cv2.convertScaleAbs(image, alpha=self.factor, beta=0)
