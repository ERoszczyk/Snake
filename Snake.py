from Attributes import Attributes


class Snake(Attributes):
    """
    This class is responsible for the size of the snake and for updating its position.
    It also controls if snake ate the food.
    """
    def __init__(self, master, width, height, food_amount, obstacle_number, snake_speed):
        super().__init__(master, width, height, food_amount, obstacle_number, snake_speed)

    def snake_cross(self):
        for number in range(len(self.position) - 1):
            if self.position[0] == self.position[-number - 1]:
                return True

    def position_update(self):
        for number in range(len(self.position) - 1):
            self.position[-number - 1] = self.position[-number - 2]

    def snake_grow(self):
        self.position.append(self.position[-1])

    def if_snake_ate_food(self):
        return super().if_food_crossed(self.position, self.food_position)

    def obstacle_colision(self):
        return super().if_crossed(self.position, self.obstacle_position)
