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
