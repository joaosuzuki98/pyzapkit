"""Send WhatsApp messages"""
import os
import platform
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import exceptions, browser_control
from typing import Union


class Pyzap(browser_control.BrowserControl):
    def __init__(
            self, profile: str = 'Default', headless: bool = False) -> None:

        self.profile = profile
        self.headless = headless
        op_sys = platform.system()

        self.options = webdriver.ChromeOptions()

        if self.headless:
            self.options.add_argument('--headless=new')
            print('Headless mode on')
        print('Headless mode off')

        if op_sys == 'Linux':
            # Setting linux home path
            home_path_linux = os.environ['HOME']

            self.options.add_argument(
                f'user-data-dir={home_path_linux}/.config/google-chrome'
            )
            self.service = Service(
                executable_path='./driver/chromedriver_linux')
        else:
            # Setting windows home path
            home_path_windows = os.environ['USERPROFILE']

            self.options.add_argument(
                f'user-data-dir={home_path_windows}'
                '\\AppData\\Local\\Google\\Chrome\\User Data'
            )
            self.service = Service(
                executable_path='./driver/chromedriver_win64')

        self.options.add_argument(f'--profile-directory={self.profile}')

    def sendmessage(
            self,
            phone_number: Union[str, int],
            message: Union[str, int],
            instantly: bool = True,
            hour: Union[str, int] = '15',
            min: Union[str, int] = '00'
    ) -> None:
        try:
            int_hour = int(hour)
            int_min = int(min)
        except ValueError as e:
            raise exceptions.TimeNotNumberException(
                'Time should only consist of numbers'
            ) from e

        if not 0 <= int_hour <= 23:
            raise exceptions.HourLimitException(
                'Write in 24-Hour format (0 - 23)'
            )

        if not 0 <= int_min <= 59:
            raise exceptions.MinLimitException(
                'Write minutes from to 0 to 59'
            )

        print('Initializing...')

        if instantly:
            self.browser_msg(
                phone_number, message, self.service, self.options)
        else:
            target_time = f'{hour}:{min}'
            print(f'Message queued to {target_time}')

            while True:
                current_time = datetime.datetime.now().time().strftime('%H:%M')

                if current_time == target_time:
                    self.browser_msg(
                        phone_number, message, self.service, self.options)
                    break
                time.sleep(1)

    def sendfile(
        self,
        phone_number: Union[int, str],
        file_pathname: str,
        load_time: int = 15,
        instantly: bool = True,
        hour: Union[str, int] = '15',
        min: Union[str, int] = '00'
    ) -> None:

        print('Initializing...')

        if instantly:
            self.browser_img_vid(phone_number, file_pathname, load_time,
                                 self.service, self.options)
        else:
            target_time = f'{hour}:{min}'
            print(f'Message queued to {target_time}')

            while True:
                current_time = datetime.datetime.now().time().strftime('%H:%M')

                if current_time == target_time:
                    self.browser_img_vid(phone_number, file_pathname,
                                         self.service, self.options)
                    break
                time.sleep(1)

    def send_doc(
        self,
        phone_number: Union[int, str],
        doc_pathname: str,
        load_time: int = 15,
        instantly: bool = True,
        hour: Union[str, int] = '15',
        min: Union[str, int] = '00'
    ) -> None:

        print('Initializing...')

        if instantly:
            self.browser_doc(phone_number, doc_pathname, load_time,
                             self.service, self.options)
        else:
            target_time = f'{hour}:{min}'
            print(f'Message queued to {target_time}')

            while True:
                current_time = datetime.datetime.now().time().strftime('%H:%M')

                if current_time == target_time:
                    self.browser_doc(phone_number, doc_pathname,
                                     self.service, self.options)
                    break
                time.sleep(1)


x = Pyzap('Profile 6')
x.send_doc('5512991527926', '/home/joao-suzuki/teste.txt')
