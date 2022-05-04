from StartWindow import StartWindow
from tkinter import Tk
import sys


def main():
    window = Tk()
    StartWindow(window)
    window.mainloop()


if __name__ == "__main__":
    sys.exit(main())
