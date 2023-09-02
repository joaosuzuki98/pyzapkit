import unittest
import os
import sys
from dotenv import load_dotenv


load_dotenv()
zap_number = os.getenv('ZAP_NUMBER')
chrome_profile = os.getenv('CHROME_PROFILE')
pyzapkit_path = os.getenv('PYZAPKIT_PATH')
img_path = os.getenv('IMG_PATH')
vid_path = os.getenv('VID_PATH')
doc_path = os.getenv('DOC_PATH')
uns_path = os.getenv('UNS_PATH')

sys.path.append(pyzapkit_path)
from pyzapkit import main
from pyzapkit.utils import exceptions


class TestPyzapkitExceptions(unittest.TestCase):
    def setUp(self):
        self.zap = main.Pyzap(chrome_profile)

    def test_wrong_chrome_profile(self):
        zap_2 = main.Pyzap('Profile 100')

        with self.assertRaises(exceptions.ChromeProfileException):
            zap_2.send_message(zap_number, 'test')

    def test_not_existing_phone_number(self):
        with self.assertRaises(exceptions.NumberNotFoundException):
            self.zap.send_message('0000', 'test')

    def test_non_number_phone_number(self):
        with self.assertRaises(exceptions.PhoneNotNumberException):
            self.zap.send_message('abcdefg', 'test')

    def test_non_number_hours(self):
        with self.assertRaises(exceptions.TimeNotNumberException):
            self.zap.send_message(zap_number, 'test', False, 'abc')

    def test_non_number_min(self):
        with self.assertRaises(exceptions.TimeNotNumberException):
            self.zap.send_message(zap_number, 'test', False, '16', 'abc')

    def test_exceeded_hour_limit(self):
        with self.assertRaises(exceptions.HourLimitException):
            self.zap.send_message(zap_number, 'test', False, '25')

    def test_exceeded_min_limit(self):
        with self.assertRaises(exceptions.MinLimitException):
            self.zap.send_message(zap_number, 'test', False, '16', '61')

    def test_not_existing_file(self):
        with self.assertRaises(exceptions.FilePathNotFoundException):
            self.zap.send_file(zap_number, '/a/directory/file.png')

    def test_unsupported_file(self):
        with self.assertRaises(exceptions.WrongFileExtensionException):
            self.zap.send_file(zap_number, uns_path)


if __name__ == '__main__':
    unittest.main()
