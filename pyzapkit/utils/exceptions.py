"""Pyzap exceptions"""


class ChromeProfileException(Exception):
    """
    This profile does not exist or does not have WhatsApp Web logged in
    """

    pass


class NumberNotFoundException(Exception):
    """
    Phone number does not exist
    """

    pass


class PhoneNotNumberException(Exception):
    """
    Phone number must only have numbers
    """

    pass


class TimeNotNumberException(Exception):
    """
    Time must only have numbers
    """

    pass


class HourLimitException(Exception):
    """
    Use 24-hour format (0 - 23)
    """

    pass


class MinLimitException(Exception):
    """
    Minutes between 0 - 59
    """

    pass


class FilePathNotFoundException(Exception):
    """
    File path provided does not exist
    """

    pass


class WrongFileExtensionException(Exception):
    """
    File extension is not supported
    """

    pass


class SystemNotSupportedException(Exception):
    """
    Supported Systems are Linux and Windows only
    """

    pass
