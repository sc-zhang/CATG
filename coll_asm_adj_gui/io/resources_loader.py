from os import path
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath('.')

    return path.join(base_path, relative_path)
