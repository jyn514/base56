#!/usr/bin/env python3

from argparse import ArgumentParser

__doc__ = "Convert text or binary into base56 encoded data"
__version__ = "0.0.1-git"

ALPHABET = b'23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'


def encode(data):
    '''
    Return data encoded in base56

    Throws TypeError if data is not string or bytes

    Parameters:
        data: string or bytes
            the data to encode

    Returns:
        str
            the data encoded in base56

    '''
    if isinstance(data, str):
        data = data.encode()

    if not isinstance(data, bytes):
        raise TypeError("data should be bytes or string")

    digit_place = 1
    number = 0
    for char in reversed(data):
        number += digit_place * char
        digit_place << 8  # move to next byte

    result = bytes()
    while number > 0:
        number, index = divmod(number, 56)
        result = bytes([ALPHABET[index]]) + result

    return result


def decode(data):
    '''
    Return data as string

    Throws ValueError if data is not a valid base56 string
    Throws UnicodeEncodeException if data is outside of the ascii range

    Parameters:
        data: string or bytes
            data to decode

    Returns:
        str or bytes
            str if valid Unicode else bytes

    '''
    for char in data:
        pass  # todo


