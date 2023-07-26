"""Browser control functions"""
import time
from utils import exceptions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from typing import Union


class BrowserControl():
    def __init__(self) -> None:
        pass

    def browser_send(
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
