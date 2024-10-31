#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    method that determines if a given data set represents
    """
    num_byt = 0
    msk1 = 1 << 7
    msk2 = 1 << 6

    for byt in data:
        byt = byt & 0xFF
        if num_byt == 0:
            if (byt & 0x80) == 0:
                continue
            elif (byt & 0xE0) == 0xC0:
                num_byt = 1
            elif (byt & 0xF0) == 0xE0:
                num_byt = 2
            elif (byt & 0xF8) == 0xF0:
                num_byt = 3
            else:
                return False
        else:
            if (byt & msk1) != msk1 or (byt & msk2) == msk2:
                return False
            num_byt -= 1
    return num_byt == 0
