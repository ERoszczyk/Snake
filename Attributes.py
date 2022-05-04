from Container import Container
import random


class Attributes(Container):
    """
    This class contains metodes connected with game attributes - food and obstacles.
    It creates lists of randomly distributed objects.
    """
    def __init__(self, master, width, height, food_amount, obstacle_number, snake_speed):
        super().__init__(master, width, height, food_amount, obstacle_number, snake_speed)

    def if_crossed(self, crossing_element, crossed_element):  # check if two elements have crossed
        self.crossed_position = []
        for crossed_position in range(len(crossed_element)):
            for crossing_position in range(len(crossing_element)):
                if crossing_element[crossing_position] == crossed_element[crossed_position]:
                    return True

    def generate_random_xy(self):
        x = 10 * random.randint(1, self.width_in_box_size - 2)
        y = 10 * random.randint(1, self.height_in_box_size - 2)
        return (x, y)

    def generate_attribut_list(self, list_to_generate, list_length):
        while len(list_to_generate) < list_length:
            self.new_attribut[0] = (self.generate_random_xy())
            if not self.if_crossed(self.new_attribut, list_to_generate):
                if not self.if_crossed(self.new_attribut, self.position):
                    if list_to_generate == self.food_position:
                        if not self.if_crossed(self.new_attribut, self.obstacle_position):
                            list_to_generate.append(self.new_attribut[0])
                    else:
                        list_to_generate.append(self.new_attribut[0])

    def if_food_crossed(self, crossing_element, crossed_element):
        for crossed_position in range(len(crossed_element)):
            for crossing_position in range(len(crossing_element)):
                if crossing_element[crossing_position] == crossed_element[crossed_position]:
                    self.eaten_food_position.append(crossing_element[crossing_position])
                    return True

    def generate_food_list(self):
        if (len(self.position) + self.obstacle_number + self.food_amount) > self.number_of_pixels:
            self.food_amount = (self.available_game_board_size - len(self.position) - self.obstacle_number)
        self.generate_attribut_list(self.food_position, self.food_amount)

    def generate_obstacle_list(self):
        self.generate_attribut_list(self.obstacle_position, self.obstacle_number)
