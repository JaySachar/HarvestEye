import unittest
from classesCHANGE import CropAnalyzer

class TestCropAnalyzer(unittest.TestCase):

    def test_file_extension_grabber(self):
        xxx = CropAnalyzer("C:/Users/.../XXX.jpg")
        self.assertEqual(xxx)


# Add more test cases here
