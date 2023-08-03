"""Browser control functions"""
import time
from utils import exceptions, funcs
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BrowserControl():
    def __init__(self) -> None:
        pass

    def browser_msg(
            self,
            zap_phone: Union[str, int],
            zap_message: Union[str, int],
            browser_service,
            browser_options
    ):
        try:
            int(zap_phone)
        except ValueError as e:
            raise exceptions.PhoneNotNumberException(
                'Phone numbers must only have numbers'
            ) from e

        driver = webdriver.Chrome(
            service=browser_service,
            options=browser_options
        )

        print('Accessing Whatsapp')
        driver.get(
            'https://web.whatsapp.com/send?phone='
            f'+{zap_phone}&text={zap_message}'
            )

        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]'
                ))
            )

            raise exceptions.ChromeProfileException(
                'Wrong profile, you must choose a chrome profile '
                'that has your WhatsApp web account logged in')
        except TimeoutException:
            print('Connecting to WhatsApp Web...')

        try:
            send_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/'
                    'footer/div[1]/div/span[2]/div/div[2]/div[2]/button/'
                    'span'
                ))
            )

            time.sleep(2)
            send_button.click()
            print('Message sent')
            time.sleep(.5)

            print('Closing browser')
            time.sleep(.5)
            driver.quit()
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
    ):
        if not isinstance(file_path, str):
            raise ValueError(
                'file path name must be a string'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an int'
            )

        try:
            int(zap_phone)
        except ValueError as e:
            raise exceptions.PhoneNotNumberException(
                'Phone numbers must only have numbers'
            ) from e

        driver = webdriver.Chrome(
            service=browser_service,
            options=browser_options
        )

        print('Accessing Whatsapp')
        driver.get(
            'https://web.whatsapp.com/send?phone='
            f'+{zap_phone}'
            )

        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]'
                ))
            )

            raise exceptions.ChromeProfileException(
                'Wrong profile, you must choose a chrome profile '
                'that has your WhatsApp web account logged in')
        except TimeoutException:
            print('Connecting to WhatsApp Web...')

        try:
            plus_btn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
                ))
            )

            plus_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            driver.quit()

        try:
            send_img_vid = WebDriverWait(driver, 15).until(
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

        funcs.img_vid_msg(file_path)

        try:
            send_img_vid_btn = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/span/'
                    'div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
                ))
            )

            send_img_vid_btn.click()
            print('File sent')
            time.sleep(.5)

        except NoSuchElementException as e:
            raise exceptions.FilePathNotFoundException(
                'File path not found'
            ) from e

        # User must add a time for the file to load
        print('Waiting for file to upload')
        time.sleep(waiting_time)

        print('Closing browser')
        time.sleep(.5)
        driver.quit()

    def browser_doc(
        self,
        zap_phone: Union[str, int],
        doc_path: str,
        waiting_time: int,
        browser_service,
        browser_options
    ):
        if not isinstance(doc_path, str):
            raise ValueError(
                'document path name must be a string'
            )

        if not isinstance(waiting_time, int):
            raise ValueError(
                'Load time must be an int'
            )

        try:
            int(zap_phone)
        except ValueError as e:
            raise exceptions.PhoneNotNumberException(
                'Phone numbers must only have numbers'
            ) from e

        driver = webdriver.Chrome(
            service=browser_service,
            options=browser_options
        )

        print('Accessing Whatsapp')
        driver.get(
            'https://web.whatsapp.com/send?phone='
            f'+{zap_phone}'
            )

        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]'
                ))
            )

            raise exceptions.ChromeProfileException(
                'Wrong profile, you must choose a chrome profile '
                'that has your WhatsApp web account logged in')
        except TimeoutException:
            print('Connecting to WhatsApp Web...')

        try:
            plus_btn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
                ))
            )

            plus_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            driver.quit()

        try:
            doc_send_btn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/'
                    'div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/'
                    'div[4]/li/div/span'
                ))
            )

            doc_send_btn.click()

        except NoSuchElementException as e:
            print(f'Error: {e}')
            driver.quit()

        time.sleep(1.5)

        funcs.doc_msg(doc_path)

        try:
            send_doc_btn = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/span/'
                    'div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
                ))
            )

            send_doc_btn.click()
            print('File sent')

        except NoSuchElementException as e:
            raise exceptions.FilePathNotFoundException(
                'File path not found'
            ) from e

        # User must add a time for the file to load
        print('Waiting for file to upload')
        time.sleep(waiting_time)

        print('Closing browser')
        time.sleep(.5)
        driver.quit()
