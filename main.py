import cv2

from ImageProccessing import ImageProcessor
from ImageProccessing.Transformations import Invert
from ImageProccessing.Transformations import Brightness

if __name__ == '__main__':
    image = cv2.imread("image.jpg")

    processor = ImageProcessor()
    processor.add_transformation(Invert())
    processor.add_transformation(Brightness(1.5))

    image = processor.process(image)

    cv2.imshow("Image1", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
