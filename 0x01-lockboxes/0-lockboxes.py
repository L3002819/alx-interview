#!/usr/bin/python3
"""This module defines a function that solve the lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all the lockboxes can be opened."""
    n = len(boxes)
    my_keys = [0]

    for key in my_keys:
        for new_key in boxes[key]:
            if new_key < n and new_key not in my_keys:
                my_keys.append(new_key)

    if len(my_keys) == n:
        return True

    return False
