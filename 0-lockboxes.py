#!/usr/bin/python3
"""
lOCKBOXES
"""


def canUnlockAll(boxes):
    """ Return True if all boxes can be opened,
        else return False
    """
    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False
