from tkinter import messagebox


class NotTxtFileError(Exception):
    def __init__(self):
        self.message = "This is not a txt file!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)


class InvalidGameBoardError(Exception):
    def __init__(self):
        self.message = "This file does not contain a valid game board!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)


class GameBoardSizeError(Exception):
    def __init__(self):
        self.message = "This file does not contain correct game board size!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)


class TooManyObstaclesError(Exception):
    def __init__(self):
        self.message = "Number of obstacles in this file is more than 50% of game board!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)


class NoSnakeError(Exception):
    def __init__(self):
        self.message = "There is no snake on game board!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)


class InvalidSnakePosition(Exception):
    def __init__(self):
        self.message = "This file contains invalid snake position!"
        super().__init__(self.message)
        messagebox.showinfo("Error", self.message)
