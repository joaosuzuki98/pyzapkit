"""Some functions for the Pyzap functioning"""
import pyautogui
import os

from utils import exceptions


def img_vid_msg(file_pathname: str) -> None:
    # Checking if file format is compatible with the type of message option
    file_extensions = ['.jpeg', '.jpg', '.png', '.mp4']
    _, file_extension = os.path.splitext(file_pathname)

    if file_extension.lower() in file_extensions:
        if os.path.isfile(file_pathname):
            pyautogui.PAUSE = 1

            # In case the dialog box isn't focused by default
            x, y = pyautogui.size()
            pyautogui.moveTo(int(x / 2), int(y / 2))
            pyautogui.click()
            print('Choosing file...')

            pyautogui.hotkey('ctrl', 'l')

            formated_pathname = file_pathname.split('/')

            for word in formated_pathname:
                pyautogui.press('divide')
                pyautogui.write(word, interval=0.050)

            print('Image/video found!')

            pyautogui.press('enter')
        else:
            raise exceptions.FilePathNotFoundException(
                'File do not exist'
            )
    else:
        raise exceptions.WrongFileExtensionException(
            'File format must be either jpeg, jpg, png or mp4'
        )


def doc_msg(doc_pathname: str) -> None:
    # Checking if doc format is compatible with the type of message option
    file_extensions = [
        '.txt', '.xls', '.xlsx', '.pdf', '.doc', '.docx', '.pptx', '.ppt']
    _, file_extension = os.path.splitext(doc_pathname)

    if file_extension.lower() in file_extensions:
        if os.path.isfile(doc_pathname):
            pyautogui.PAUSE = 1

            # In case the dialog box isn't focused by default
            x, y = pyautogui.size()
            pyautogui.moveTo(int(x / 2), int(y / 2))
            pyautogui.click()
            print('Choosing file...')

            pyautogui.hotkey('ctrl', 'l')

            formated_pathname = doc_pathname.split('/')

            for word in formated_pathname:
                pyautogui.press('divide')
                pyautogui.write(word, interval=0.050)

            print('Image/video found!')

            pyautogui.press('enter')
        else:
            raise exceptions.FilePathNotFoundException(
                'File do not exist'
            )
    else:
        raise exceptions.WrongFileExtensionException(
            'File format must be either txt, doc, '
            'docx, pdf, xls, xlsx, ppt or pptx'
        )
