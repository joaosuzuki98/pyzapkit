"""Browser control functions"""
import time
from utils import exceptions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BrowserControl():
    def __init__(self) -> None:
        pass

    def browser_send(
            self,
            zap_phone: str,
            zap_message: str,
            browser_service,
            browser_options
    ):
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
            send_button = WebDriverWait(driver, 20).until(
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
            raise exceptions.ChromeProfileException(
                'Wrong profile, you must choose a chrome profile '
                'that has your WhatsApp web account logged in'
            ) from e
