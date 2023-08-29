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


if __name__ == '__main__':
    unittest.main()
