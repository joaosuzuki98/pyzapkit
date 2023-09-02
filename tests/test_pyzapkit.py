import unittest
import os
import sys
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
zap_number = os.getenv('ZAP_NUMBER')
chrome_profile = os.getenv('CHROME_PROFILE')
pyzapkit_path = os.getenv('PYZAPKIT_PATH')
img_path = os.getenv('IMG_PATH')
vid_path = os.getenv('VID_PATH')
doc_path = os.getenv('DOC_PATH')

sys.path.append(pyzapkit_path)
from pyzapkit import main


class TestPyzapkitHeadlessOff(unittest.TestCase):
    def setUp(self):
        self.zap = main.Pyzap(chrome_profile)

    def test_send_whatsapp_message_instantly(self):
        self.zap.send_message(zap_number, 'test')

    def test_send_whatsapp_img_instantly(self):
        self.zap.send_file(zap_number, img_path)

    def test_send_whatsapp_video_instantly(self):
        self.zap.send_file(zap_number, vid_path)

    def test_send_whatsapp_doc_instantly(self):
        self.zap.send_doc(zap_number, doc_path)

    def test_send_whatsapp_message_scheduled(self):
        hour_schedule = datetime.now().hour
        min_schedule = datetime.now().minute + 1
        self.zap.send_message(
            zap_number, 'test', False, hour_schedule, min_schedule)

    def test_send_whatsapp_img_scheduled(self):
        hour_schedule = datetime.now().hour
        min_schedule = datetime.now().minute + 1
        self.zap.send_file(
            zap_number, img_path, False, hour_schedule, min_schedule)

    def test_send_whatsapp_video_scheduled(self):
        hour_schedule = datetime.now().hour
        min_schedule = datetime.now().minute + 1
        self.zap.send_file(
            zap_number, vid_path, False, hour_schedule, min_schedule)

    def test_send_whatsapp_doc_scheduled(self):
        hour_schedule = datetime.now().hour
        min_schedule = datetime.now().minute + 1
        self.zap.send_doc(
            zap_number, doc_path, False, hour_schedule, min_schedule)


if __name__ == '__main__':
    unittest.main()
