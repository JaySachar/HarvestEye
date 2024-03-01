import unittest
from classesCHANGE import ImageStitcher

class TestImageStitcher(unittest.TestCase):

    def test_file_extension_grabber(self):
        xxx = ImageStitcher("C:/Users/.../XXX.jpg")
        self.assertEqual(xxx)


# Add more test cases here
