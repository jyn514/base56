from argparse import ArgumentParser

__description__ = "Convert text or binary into base56 encoded data"
__version__ = "0.0.1-git"

ALPHABET = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
pad = '='


def main():
    pass  # todo


def encode(data):
    '''
    Return data encoded in base56

    Throws TypeError is data is not string or bytes

    Parameters:
        data: string or bytes
            the data to encode

    Returns:
        str
            the data encoded in base56

    '''
    if type(data) == str:
        data = data.encode()

    if type(data) != bytes:
        raise TypeError("data should be bytes or string")

    for char in data:
        pass  # todo


def decode(data):
    '''
    Return data as string

    Throws ValueError if data is not a valid base56 string

    Parameters:
        data: string
            data to decode

    Returns:
        str or bytes
            str if valid Unicode else bytes

    '''
    for char in data:
        pass  # todo


if __name__ == "__main__":
    main()
