import cv2
from . import TransformationInterface


class Invert(TransformationInterface):
    def apply(self, image):
        return cv2.bitwise_not(image)
