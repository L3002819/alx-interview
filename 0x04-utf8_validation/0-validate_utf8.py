#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (List[int]): A list of integers representing the data set.
    
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate through each integer in the data
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If we finish processing and there are remaining bytes, return False
    return num_bytes == 0
