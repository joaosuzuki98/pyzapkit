"""Browser control methods"""
import time
from utils import exceptions, funcs
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BrowserControl():
    """Browser automation through selenium"""
    def __init__(self) -> None:
        pass

    def _open_whatsappweb(
            self, phone: Union[str, int], message: Union[str, int], 
            br_service, br_options):
        """
        Opens Whatsapp web with the given phone number and message

        :param phone: the receiver phone number
        :type phone: Union[str, int]
        :param message: The message to be sent
        :type message: Union[str, int]
        :param br_service: Selenium browser services
        :type br_service: Any
        :param br_options: Selenium browser options
        :type br_options: Any
        """
        try:
            int(phone)
        except ValueError as e:
            raise exceptions.PhoneNotNumberException(
                'Phone numbers must only have numbers'
            ) from e

        self.driver = webdriver.Chrome(
            service=br_service,
            options=br_options
        )

        print('Accessing Whatsapp')
        self.driver.get(
            'https://web.whatsapp.com/send?phone='
            f'+{phone}' + (f'&text={message}' if message else '')
            )

        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]'
                ))
            )

            raise exceptions.ChromeProfileException(
                'Wrong profile, you must choose a chrome profile '
                'that has your WhatsApp web account logged in')
        except TimeoutException:
            print('Connecting to WhatsApp Web...')

    def _send_file_btn(self, load_time: int) -> None:
        """
        Click on the send button

        :param load_time: The time to wait before closing the browser
        :type load_time: int
        """
        try:
            send_file_btn = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/span/'
                    'div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
                ))
            )

            send_file_btn.click()
            print('File sent')

            # User must add a time for the file to load
            print('Waiting for file to upload')
            time.sleep(load_time)

            print('Closing browser')
            time.sleep(.5)
            self.driver.quit()

        except NoSuchElementException as e:
            raise exceptions.FilePathNotFoundException(
                'File path not found'
            ) from e

    def browser_msg(
            self,
            zap_phone: Union[str, int],
            zap_message: Union[str, int],
            browser_service,
            browser_options,
    ) -> None:
        """
        Sends the text message

        :param zap_phone: The receiver phone number
        :type zap_phone: Union[str, int]
        :param zap_message:  The message to be sent
        :type zap_message: Union[str, int]
        :param br_service: Selenium browser services
        :type br_service: Any
        :param br_options: Selenium browser options
        :type br_options: Any
        """
        self._open_whatsappweb(
            zap_phone, zap_message, browser_service, browser_options)

        try:
            send_button = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/'
                    'footer/div[1]/div/span[2]/div/div[2]/div[2]/button/'
                    'span'
                ))
            )

            time.sleep(2)
            send_button.click()
            print('Message sent')
            time.sleep(1)

            print('Closing browser')
            time.sleep(.5)
            self.driver.quit()
        except TimeoutException as e:
            raise exceptions.NumberNotFoundException(
                'Phone number does not exist'
            ) from e

    def browser_img_vid(
            self,
            zap_phone: Union[str, int],
            file_path: str,
            waiting_time: int,
            browser_service,
            browser_options
    ) -> None:
        """
        Sends the image or video

        :param zap_phone: The receiver phone number
        :type zap_phone: Union[str, int]
        :param file_path: The path of the file to be sent
        :type file_path: str
        :param waiting_time: The time to wait for the the file to be uploaded
        before closing the browser
        :type waiting_time: int
        :param br_service: Selenium browser services
        :type br_service: Any
        :param br_options: Selenium browser options
        :type br_options: Any
        """
        if not isinstance(file_path, str):
            raise ValueError(
                'file path name must be a string'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an int'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an integer'
            )

        self._open_whatsappweb(zap_phone, '', browser_service, browser_options)

        try:
            plus_btn = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
                ))
            )

            plus_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            self.driver.quit()

        try:
            send_img_vid = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/'
                    'div[1]/li/div/span'
                ))
            )

            send_img_vid.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')

        time.sleep(1.5)

        funcs._file_getter(file_path, 'img-vid')

        self._send_file_btn(waiting_time)

    def browser_doc(
        self,
        zap_phone: Union[str, int],
        doc_path: str,
        waiting_time: int,
        browser_service,
        browser_options
    ) -> None:
        """
        Sends the chosen document

        :param zap_phone: The receiver phone number
        :type zap_phone: Union[str, int]
        :param doc_path: The path to the document
        :type doc_path: str
        :param waiting_time: The time the browser will wait for the document
        to be uploaded before closing
        :type waiting_time: int
        :param br_service: Selenium browser services
        :type br_service: Any
        :param br_options: Selenium browser options
        :type br_options: Any
        """
        if not isinstance(doc_path, str):
            raise ValueError(
                'document path name must be a string'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an int'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an integer'
            )

        self._open_whatsappweb(zap_phone, '', browser_service, browser_options)

        try:
            plus_btn = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
                ))
            )

            plus_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            self.driver.quit()

        try:
            doc_send_btn = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/'
                    'div[4]/li/div/span'
                ))
            )

            doc_send_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            self.driver.quit()

        time.sleep(1.5)

        funcs._file_getter(doc_path, 'doc')

        self._send_file_btn(waiting_time)
