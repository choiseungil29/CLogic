import os
import sys

from Utils.Log import Logger
from Window.Window import Window


def main():
    window = None
    try:
        window = Window(int(sys.argv[1]), int(sys.argv[2]))
    except IndexError as e:
        # Logger.Error(e.message + " " + "(Cngine: 15)")
        window = Window(800, 600)
    finally:
        window.createWindow()


if __name__ == '__main__':
    main()





