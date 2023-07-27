"""Some functions for the Pyzap functioning"""
import pyperclip


def clipboard_copy(file_pathname):
    try:
        with open(file_pathname, 'rb') as file:
            file_content = file.read()
            file_content_base64 = file_content.encode('base64')

            pyperclip.copy(file_content_base64)
            print(f'{file_pathname} copied to the clipboard')
    except Exception as e:
        print(f'An error ocurred while copying the file: {e}')
