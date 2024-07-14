import unittest
from classesCHANGE import ImageProcessor

class TestImageProcessor(unittest.TestCase):

    def test_file_extension_grabber(self):
        processor = ImageProcessor("C:/Users/.../XXX.jpg")
        self.assertEqual(processor.file_extension_grabber("C:/Users/.../XXX.jpg"), ".jpg")


# Add more test cases here
