#!/usr/bin/python3
"""
method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    :return: True if all boxes can be opened, else False
    """
    ob = [False] * len(boxes)
    ob[0] = True
    stack = [0]

    while stack:
        cb = stack.pop()
        for key in boxes[cb]:
            if key < len(boxes) and not ob[key]:
                ob[key] = True
                stack.append(key)
    return all(ob)
