import random


class Container:
    """
    This class contains the most important variables that are used in other classes.
    """
    def __init__(self, master, width, height, food_amount, obstacle_number, snake_speed):
        self.master = master
        self.width = width
        self.height = height
        self.obstacle_number = obstacle_number
        self.food_amount = food_amount
        self.snake_speed = snake_speed

        self.position = []
        self.starting_position = []
        self.obstacle_position = []
        self.food_position = []
        self.eaten_food_position = []
        self.file_lines = []
        self.new_attribut = [(0, 0)]
        self.available_game_board_size = ["30 30", "40 40", "50 50", "60 60"]

        self.move_direction = random.randint(0, 1)
        self.selected_snake_speed = 100
        self.box_size = 10
        self.width_in_box_size = int(self.width / self.box_size)
        self.height_in_box_size = int(self.height / self.box_size)
        self.number_of_pixels = int((self.width / self.box_size - 2) * (self.height / self.box_size - 2))

        self.game_lost = False
        self.game_won = False
        self.game_started = False
        self.if_game_finished = False
        self.if_file = False
        self.pause = False

        self.user_input = ""
        self.file_path = ""
