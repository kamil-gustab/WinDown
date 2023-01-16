import unittest
from datetime import datetime
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import operations
from windown import Window

app = QApplication([])

class TestWindow(unittest.TestCase):
    def setUp(self):
        self.window = Window()

    def test_creation(self):
        self.assertIsInstance(self.window, Window)

    def test_hour_plus(self):
        self.window.hour = 0
        self.window.hour_plus()
        self.assertEqual(self.window.hour, 1)

        self.window.hour = 23
        self.window.hour_plus()
        self.assertEqual(self.window.hour, 23)

    def test_hour_minus(self):
        self.window.hour = 1
        self.window.hour_minus()
        self.assertEqual(self.window.hour, 0)

        self.window.hour = 0
        self.window.hour_minus()
        self.assertEqual(self.window.hour, 0)

    def test_min_plus(self):
        self.window.minute = 0
        self.window.min_plus()
        self.assertEqual(self.window.minute, 1)

        self.window.minute = 59
        self.window.min_plus()
        self.assertEqual(self.window.minute, 59)

    def test_min_minus(self):
        self.window.minute = 1
        self.window.min_minus()
        self.assertEqual(self.window.minute, 0)

        self.window.minute = 0
        self.window.min_minus()
        self.assertEqual(self.window.minute, 0)

    def test_reset_time(self):
        self.window.hour = 1
        self.window.minute = 1
        self.window.reset_time()
        self.assertEqual(self.window.hour, int(datetime.now().strftime("%H")))
        self.assertEqual(self.window.minute, int(datetime.now().strftime("%M")))

    def test_request_shutdown(self):
        self.window.hour = int(datetime.now().strftime("%H")) + 1
        self.window.minute = int(datetime.now().strftime("%M"))
        self.window.request_shutdown()

    def test_request_shutdown(self):
        self.window.cancel_shutdown()


if __name__ == '__main__':
    unittest.main()