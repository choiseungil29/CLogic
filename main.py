import os
import sys

from Utils.Log import Logger
from Window.Window import Window


def main():
    window = None
    try:
        window = Window(int(sys.argv[1]), int(sys.argv[2]))
    except IndexError as e:
        window = Window(1280, 800)
    finally:
        window.createWindow()


if __name__ == '__main__':
    main()