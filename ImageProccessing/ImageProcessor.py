from .Transformations import TransformationInterface


class ImageProcessor:
    def __init__(self):
        self.transformations = list()

    def add_transformation(self, transformation: TransformationInterface):
        self.transformations.append(transformation)

    def process(self, image):
        for transformation in self.transformations:
            image = transformation.apply(image)

        return image
