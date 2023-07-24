"""Send WhatsApp messages"""
import os
import platform
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# TODO adicionar os tipos
class Pyzap():
    def __init__(
            self, profile: str = 'Default', headless: bool = True) -> None:

        self.profile = profile
        self.headless = headless
        op_sys = platform.system()

        options = webdriver.ChromeOptions()

        if self.headless:
            options.add_argument('--headless=new')
            print('Headless mode on')
        print('Headless mode off')

        if op_sys == 'Linux':
            # Setting linux home path
            home_path_linux = os.environ['HOME']

            options.add_argument(
                f'user-data-dir={home_path_linux}/.config/google-chrome'
            )
            service = Service(executable_path='./driver/chromedriver_linux')
        else:
            # Setting windows home path
            home_path_windows = os.environ['USERPROFILE']

            options.add_argument(
                f'user-data-dir={home_path_windows}'
                '\\AppData\\Local\\Google\\Chrome\\User Data'
            )
            service = Service(executable_path='./driver/chromedriver_win64')

        options.add_argument(f'--profile-directory={self.profile}')

        self.driver = webdriver.Chrome(
            service=service,
            options=options
        )

    def sendmessage(
            self,
            phone_number: str,
            message: str,
            instantly: bool = True
    ) -> None:
        print('Initializing...')

        if instantly:
            self.driver.get(
                'https://web.whatsapp.com/send?phone='
                f'+{phone_number}&text={message}'
                )

            try:
                send_button = WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((
                        By.XPATH, '/html/body/div[1]/div/div/div[5]/div/'
                        'footer/div[1]/div/span[2]/div/div[2]/div[2]/button/'
                        'span'
                    ))
                )
                send_button.click()
                print('Message sent')
                time.sleep(.5)

                print('Closing browser')
                time.sleep(.5)
                self.driver.quit()

            except NoSuchElementException:
                print('An error ocurred')
                time.sleep(.5)
                self.driver.quit()


x = Pyzap('Profile 6', False)
