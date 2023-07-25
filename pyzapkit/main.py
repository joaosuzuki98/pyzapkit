"""Send WhatsApp messages"""
import os
import platform
import time
import datetime
from utils import exceptions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Pyzap():
    def __init__(
            self, profile: str = 'Default', headless: bool = True) -> None:

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
            phone_number: str,
            message: str,
            instantly: bool = True,
            hour: str = '15',
            min: str = '30'
    ) -> None:
        print('Initializing...')

        if instantly:
            self.driver = webdriver.Chrome(
                service=self.service,
                options=self.options
            )

            print('Accessing Whatsapp')
            self.driver.get(
                'https://web.whatsapp.com/send?phone='
                f'+{phone_number}&text={message}'
                )

            try:
                send_button = WebDriverWait(self.driver, 20).until(
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
                self.driver.quit()
            except TimeoutException as e:
                raise exceptions.ChromeProfileException(
                    'Wrong profile, you must choose a chrome profile '
                    'that has your WhatsApp web account logged in'
                ) from e
        else:
            target_time = f'{hour}:{min}'
            print(f'Message queued to {target_time}')

            while True:
                current_time = datetime.datetime.now().time().strftime('%H:%M')

                if current_time == target_time:
                    self.driver = webdriver.Chrome(
                        service=self.service,
                        options=self.options
                    )

                    print('Accessing Whatsapp')
                    self.driver.get(
                        'https://web.whatsapp.com/send?phone='
                        f'+{phone_number}&text={message}'
                        )

                    try:
                        send_button = WebDriverWait(self.driver, 20).until(
                            EC.presence_of_element_located((
                                By.XPATH, '/html/body/div[1]/div/div/div[5]/'
                                'div/footer/div[1]/div/span[2]/div/div[2]/'
                                'div[2]/button/span'
                            ))
                        )

                        time.sleep(2)
                        send_button.click()
                        print('Message sent')
                        time.sleep(.5)

                        print('Closing browser')
                        time.sleep(.5)
                        self.driver.quit()
                        break
                    except TimeoutException as e:
                        raise exceptions.ChromeProfileException(
                            'Wrong profile, you must choose a chrome profile '
                            'that has your WhatsApp web account logged in'
                        ) from e

                time.sleep(1)


x = Pyzap('Profile 6', False)
