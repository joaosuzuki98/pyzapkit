"""PyAutoGui functions"""
import pyautogui
import os
import platform

from utils import exceptions


def _file_getter(file_pathname: str, file_type: str) -> None:
    """
    Checks if the file exist and if its extension is supported. If so, then
    It will upload that file

    :param file_pathname: The path to the file
    :type file_pathname: str
    :param file_type: The type of file (document or image/video)
    :type file_type: str
    """
    # Checking if file format is compatible with the type of message option
    file_extensions = []
    if file_type == 'doc':
        file_extensions.extend((
            '.txt', '.xls', '.xlsx', '.pdf', '.doc', '.docx', '.pptx', '.ppt'))
    else:
        file_extensions.extend(('.jpeg', '.jpg', '.png', '.mp4'))

    _, file_extension = os.path.splitext(file_pathname)

    op_sys = platform.system()

    if file_extension.lower() in file_extensions:
        if os.path.isfile(file_pathname):

            pyautogui.PAUSE = 1

            if op_sys == 'Linux':
                # In case the dialog box isn't focused by default
                x, y = pyautogui.size()
                pyautogui.moveTo(int(x / 2), int(y / 2))
                pyautogui.click()
                print('Choosing file...')

                pyautogui.hotkey('ctrl', 'l')

                formated_pathname = file_pathname.split('/')

                for word in formated_pathname:
                    pyautogui.press('divide')
                    pyautogui.write(word, interval=0.05)

                print('Image/video found!')

                pyautogui.press('enter')

            elif op_sys == 'Windows':
                pyautogui.write(file_pathname, interval=0.05)
                pyautogui.press('enter')

            else:
                raise exceptions.SystemNotSupportedException(
                    'Only Windows and Linux systems are supported'
                )
        else:
            raise exceptions.FilePathNotFoundException(
                'File do not exist'
            )
    else:
        if file_type == 'img-vid':
            raise exceptions.WrongFileExtensionException(
                'File format must be either jpeg, jpg, png or mp4'
            )
        else:
            raise exceptions.WrongFileExtensionException(
                'File format must be either txt, doc, '
                'docx, pdf, xls, xlsx, ppt or pptx'
            )
