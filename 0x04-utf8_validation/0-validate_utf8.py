#!/usr/bin/python3
"""This Module defines the `validUTF8` function."""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data: a list of integers,
              Each integer is [0-255] represents 1 byte of data (0-255),
              so we only handle the 8 least significant bits of each integer.
              can contain multiple characters.
              A character in UTF-8 can be 1 to 4 bytes long.

    Return:
        True if data is a valid UTF-8 encoding, else return False
    """
    for i in range(len(data)):
        if data[i] < 0 or data[i] > 255:
            # handle only the 8 least significant bits
            data[i] = int(bin(data[i])[-8:], 2)

    try:
        bytes(data).decode(encoding='utf-8', errors='strict')
        return True
    except Exception:
        return False
