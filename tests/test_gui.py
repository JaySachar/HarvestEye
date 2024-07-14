import unittest
from classesCHANGE import GUI

class TestGUI(unittest.TestCase):

    def test_file_extension_grabber(self):
        xxx = GUI("C:/Users/.../XXX.jpg")
        self.assertEqual(xxx)


# Add more test cases here
