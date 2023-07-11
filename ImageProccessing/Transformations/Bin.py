import cv2
from . import TransformationInterface


class Bin(TransformationInterface):
    def __init__(self, threshold):
        self.threshold = threshold

    def apply(self, image):
        _, binary_image = cv2.threshold(image, self.threshold, 255, cv2.THRESH_BINARY)
        return binary_image
