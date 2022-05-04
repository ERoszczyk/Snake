from tkinter import Canvas
from ReadFromFile import ReadFromFile


class Graphics(ReadFromFile):
    """
    This class is responsible for the graphics side of the game.
    It creates game board, snake, food and obstacles.
    """
    def __init__(self, master, width, height, food_amount, obstacle_number, snake_speed):
        super().__init__(master, width, height, food_amount, obstacle_number, snake_speed)

        master.title("Snake")
        master.iconbitmap(r'snake_icon.ico')
        master.geometry(f"{self.width}x{self.height+20}")

        self.pixel = Canvas(master, width=self.width, height=self.height)
        self.pixel.pack()

    def create_one_pixel(self, x, y, color="Black"):
        self.pixel.create_rectangle([x, y, x + self.box_size, y + self.box_size], fill=color)

    def create_game_border(self):
        for width in range(self.width_in_box_size):
            self.create_one_pixel(width * self.box_size, 0)
            self.create_one_pixel(width * self.box_size, (self.height_in_box_size - 1) * self.box_size)
        for height in range(self.height_in_box_size):
            self.create_one_pixel(0, self.box_size * height)
            self.create_one_pixel(width * self.box_size, self.box_size * height)

    def create_snake(self):
        for position in self.position:
            self.create_one_pixel(position[0], position[1], "Red")

    def create_supplements_from_list(self, supplement_position, color):  # można przerobić na jedną
        number = 0
        while number < len(supplement_position):
            self.create_one_pixel(supplement_position[number][0], supplement_position[number][1], color)
            number += 1

    def create_food(self):
        super().generate_food_list()
        self.create_supplements_from_list(self.food_position, "Green")

    def create_obstacles(self):
        if not self.if_file:
            super().generate_obstacle_list()
        self.create_supplements_from_list(self.obstacle_position, "Yellow")
