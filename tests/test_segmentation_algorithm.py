import unittest
from classesCHANGE import SegmentationAlgorithm

class TestSegmentation(unittest.TestCase):

    def test_file_extension_grabber(self):
        xxx = SegmentationAlgorithm("C:/Users/.../XXX.jpg")
        self.assertEqual(xxx)


# Add more test cases here
