from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from Snake import Snake
from Errors import NotTxtFileError, InvalidGameBoardError, GameBoardSizeError, TooManyObstaclesError, NoSnakeError, InvalidSnakePosition


class ReadFromFile(Snake):
    """
    This class contains methods to open file and collect data from it.
    It also raises an exception when there are problems with file.
    """
    def __init__(self, master, width, height, food_amount, obstacle_number, snake_speed):
        super().__init__(master, width, height, food_amount, obstacle_number, snake_speed)

    def ask_for_file(self):
        self.user_input = ""
        self.user_input = askopenfilename()

    def if_txt(self):
        if self.user_input[-4:] == ".txt":
            self.file_path = self.user_input
            return True

    def open_file(self):
        self.file_lines = []
        self.file = open(self.file_path, "r", encoding="utf-8")
        self.coordinates = self.file.readline()
        self.coordinates = self.coordinates.strip("\n")
        if self.if_correct_coordinates():
            self.x_coordinate = int(self.coordinates[0:2])
            self.y_coordinate = int(self.coordinates[3:5])
            for y in range(self.y_coordinate):
                self.file_lines.append(self.file.readline())
        else:
            self.file.close()
            raise GameBoardSizeError
        self.file.close()

    def if_correct_coordinates(self):
        for coordinate in self.available_game_board_size:
            if self.coordinates == coordinate:
                return True
        else:
            return False

    def if_boarden(self):
        for y in range(self.y_coordinate):
            line = self.file_lines[y]
            if y == 0 or y == self.y_coordinate:
                if line[0:self.x_coordinate] != ("\u2588" * self.x_coordinate):
                    return False
            else:
                if line[0:2] != ("\u2588" * 2):
                    return False
        else:
            return True

    def if_correct_game_board(self):
        for y in range(1, self.y_coordinate - 1):
            line = self.file_lines[y]
            for x in range(2, 2 * self.x_coordinate - 2, 2):
                if line[x:x + 2] != ("\u2591" * 2) and line[x:x + 2] != ("\u2550" * 2) and line[x:x + 2] != ("\u2551" * 2):
                    return False
        else:
            return True

    def if_file_correct(self):
        if self.if_txt():
            try:
                self.open_file()
                if self.if_boarden() and self.if_correct_game_board():
                    self.if_file = True
                    return True
                else:
                    raise InvalidGameBoardError
            except FileNotFoundError as e:
                messagebox.showinfo("Error", e)
        else:
            raise NotTxtFileError

    def if_snake_position_correct(self):
        for position_number in range(len(self.position) - 1):
            if self.position[position_number + 1] != (self.position[position_number][0], self.position[position_number][0] + 10):
                return False
        else:
            return True

    def load_obtacles_from_file(self):
        self.open_file()
        self.obstacle_position = []
        for y in range(self.y_coordinate):
            line = self.file_lines[y]
            for x in range(0, 2 * self.x_coordinate, 2):
                if line[x:x + 2] == ("\u2550" * 2):
                    self.obstacle_position.append((int(x * 5), y * 10))
        if len(self.obstacle_position) >= self.number_of_pixels / 2:
            raise TooManyObstaclesError

    def load_snake_from_file(self):
        self.open_file()
        self.position = []
        self.starting_position = []
        for y in range(self.y_coordinate):
            line = self.file_lines[y]
            for x in range(0, 2 * self.x_coordinate, 2):
                if line[x:x + 2] == ("\u2551" * 2):
                    self.position.append((int(x * 5), y * 10))
                    self.starting_position.append((int(x * 5), y * 10))
        if len(self.position) == 0:
            raise NoSnakeError
        if len(self.position) >= self.height / 3:
            raise TooManyObstaclesError

    def read_game_board_from_file(self):
        self.file_lines = []
        self.if_file_correct()
        if self.if_file:
            self.load_obtacles_from_file()
            self.load_snake_from_file()
            if not self.if_snake_position_correct:
                raise InvalidSnakePosition
            self.if_file = True
        else:
            self.if_file = False
