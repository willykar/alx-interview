#!/usr/bin/python3
""" 0-lockboxes module """


def canUnlockAll(boxes):
    """A method that determines if all boxes can be opened
        boxes: A list of lists
        Return: True if all boxes can be opened,else return False
    """
    if not boxes or type(boxes) is not list:
        return False
    unlocked_boxes = [0]
    for i in unlocked_boxes:
        for key in boxes[i]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == len(boxes)
