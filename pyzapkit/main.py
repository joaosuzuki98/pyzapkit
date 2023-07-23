"""Send WhatsApp messages"""
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Zap():
    def __init__(self, profile='Default', headless=True):
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
                {f'user-data-dir={home_path_windows}'
                 '\\AppData\\Local\\Google\\Chrome\\User Data'}
            )
            service = Service(executable_path='./driver/chromedriver_win64')

        options.add_argument(f'--profile-directory={self.profile}')

        driver = webdriver.Chrome(
            service=service,
            options=options
        )

        print('Initializing...')
        driver.get('https://www.globo.com/')


x = Zap('Profile 6', False)
