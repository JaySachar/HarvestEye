import unittest
from classesCHANGE import PointCloudGenerator

class TestPointCloudGenerator(unittest.TestCase):

    def test_file_extension_grabber(self):
        xxx = PointCloudGenerator("C:/Users/.../XXX.jpg")
        self.assertEqual(xxx)


# Add more test cases here
