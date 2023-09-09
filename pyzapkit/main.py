"""
Send WhatsApp messages, documents, videos and images
====================================================

Pyzapkit offers an automated way to send messages through Whatsapp.

It contains methods to send images or videos, documents and normal text
messages. It is possible to send them instantly or in a given time
"""
import sys
import os

pyzapkit_path = os.path.abspath(os.getcwd())
sys.path.append(pyzapkit_path)

import platform
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyzapkit.utils import exceptions, browser_control
from typing import Union, Callable


class Pyzap(browser_control.BrowserControl):
    """
    Set the time in which the messages will be sent.

    It stores time data in 24 format, phone number, message text or file path

    :param profile: Google Chrome profile to be used
    :type profile: str
    :param headless: Activate Google Chrome headless mode
    :type headless: bool
    """
    def __init__(
            self, profile: str = 'Default') -> None:
        """
        Constructs the necessary atributes of the Pyzap class.       

        :param profile: Google Chrome profile to be used
        :type profile: str
        """
        self.profile = profile
        op_sys = platform.system()

        self.options = webdriver.ChromeOptions()

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

    def _send(
            self, instantly: bool, hour: Union[int, str], 
            min: Union[int, str], func: Callable, 
            *args: Union[int, str]) -> None:
        """
        Set time for the message or file

        :param instantly: Set if the message will be sent instantly or at a 
        given time
        :type instantly: bool
        :param hour: The hour in which the message or file will be sent
        :type hour: Union[int, str]
        :param min: The minutes that will be used along the hours
        :type min: Union[int, str]
        :param func: A function that will set the sending type
        :type func: Callable
        :param *args: The necessary arguments for the func parameter
        :type *args: Union[int, str]
        """
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
            func(*args)
        else:
            target_time = f'{hour}:{min}'
            print(f'Message queued to {target_time}')

            while True:
                current_time = datetime.datetime.now().time().strftime('%H:%M')

                if current_time == target_time:
                    func(*args)
                    break
                time.sleep(1)

    def send_message(
            self,
            phone_number: Union[str, int],
            message: Union[str, int],
            instantly: bool = True,
            hour: Union[str, int] = '15',
            min: Union[str, int] = '00'
    ) -> None:
        """
        Send text messages to a given phone number

        :param phone_number: The phone number that will receive the message
        :type phone_number: Union[str, int]
        :param message: The text message to be used in Whatsapp
        :type message: Union[str, int]
        :param instantly: If the message will be sent instantly or at a given 
        time
        :type instantly: bool
        :param hour: The hour in which the message will be sent
        :type hour: Union[int, str]
        :param min: The minutes that will be used along the hours
        :type min: Union[int, str]
        """
        self._send(
            instantly, hour, min, self.browser_msg, phone_number, message,
            self.service, self.options)

    def send_file(
        self,
        phone_number: Union[int, str],
        file_pathname: str,
        load_time: int = 15,
        instantly: bool = True,
        hour: Union[str, int] = '15',
        min: Union[str, int] = '00'
    ) -> None:
        """
        Send images or videos to a given phone number

        :param phone_number: The phone number that will receive the file
        :type phone_number: Union[str, int]
        :param file_pathname: The file to be sent in Whatsapp
        :type file_pathname: str
        :param load_time: The time selenium will wait before closing the
        browser, so the file sent can be uploaded
        :type load_time: int
        :param instantly: If the file will be sent instantly or at a given 
        time
        :type instantly: bool
        :param hour: The hour in which the file will be sent
        :type hour: Union[int, str]
        :param min: The minutes that will be used along the hours
        :type min: Union[int, str]
        """
        self._send(
            instantly, hour, min, self.browser_img_vid, phone_number,
            file_pathname, load_time, self.service, self.options)

    def send_doc(
        self,
        phone_number: Union[int, str],
        doc_pathname: str,
        load_time: int = 15,
        instantly: bool = True,
        hour: Union[str, int] = '15',
        min: Union[str, int] = '00'
    ) -> None:
        """
        Send document to a given phone number

        :param phone_number: The phone number that will receive the document
        :type phone_number: Union[int, str],
        :param doc_pathname: The path to the document
        :type doc_pathname: str
        :param load_time: The time selenium will wait before closing the
        browser, so the document sent can be uploaded
        :type load_time: int
        :param instantly: If the document will be sent instantly or at a given
        time
        :type instantly: bool
        :param hour: The hour in which the document will be sent
        :type hour: Union[int, str]
        :param min: The minutes that will be used along the hours
        :type min: Union[int, str]
        """
        self._send(
            instantly, hour, min, self.browser_doc, phone_number,
            doc_pathname, load_time, self.service, self.options)
