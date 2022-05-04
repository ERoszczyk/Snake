from tkinter import messagebox
from Graphics import Graphics
import random


class Game(Graphics):
    """
    This class contains methods related to the snake movement.
    It also contols modes such as win or lose.
    """
    def __init__(self, master, width=300, height=300, food_amount=3, obstacle_number=5, snake_speed=150):
        super().__init__(master, width, height, food_amount, obstacle_number, snake_speed)

        master.bind_all("<KeyPress-Down>", self.key_go_down)
        master.bind_all("<KeyPress-Up>", self.key_go_up)
        master.bind_all("<KeyPress-Right>", self.key_turn_right)
        master.bind_all("<KeyPress-Left>", self.key_turn_left)

    def snake_ate_food(self):
        if self.if_snake_ate_food():
            (x, y) = (int(self.eaten_food_position[0][0]), int(self.eaten_food_position[0][1]))
            self.food_position.remove((x, y))
            self.eaten_food_position.remove((x, y))
            super().snake_grow()

    def go_up(self):
        if not self.pause:
            self.position_update()
            if self.position[0][1] != 10:
                self.position[0] = (self.position[0][0], self.position[0][1] - 10)
            else:
                self.position[0] = (self.position[0][0], self.height - 20)
            self.move_direction = 0
            self.reset()
            self.create_snake()

    def go_down(self):
        if not self.pause:
            self.position_update()
            if self.position[0][1] != self.height - 20:
                self.position[0] = (self.position[0][0], self.position[0][1] + 10)
            else:
                self.position[0] = (self.position[0][0], 10)
            self.move_direction = 2
            self.reset()
            self.create_snake()

    def turn_right(self):
        if not self.pause:
            self.position_update()
            if self.position[0][0] != self.width - 20:
                self.position[0] = (self.position[0][0] + 10, self.position[0][1])
            else:
                self.position[0] = (10, self.position[0][1])
            self.move_direction = 1
            self.reset()
            self.create_snake()

    def turn_left(self):
        if not self.pause:
            self.position_update()
            if self.position[0][0] != 10:
                self.position[0] = (self.position[0][0] - 10, self.position[0][1])
            else:
                self.position[0] = (self.width - 20, self.position[0][1])
            self.move_direction = 3
            self.reset()
            self.create_snake()

    def key_go_down(self, event):
        if self.move_direction == 1 or self.move_direction == 3:
            self.go_down()

    def key_go_up(self, event):
        if self.move_direction == 1 or self.move_direction == 3:
            self.go_up()

    def key_turn_right(self, event):
        if self.move_direction == 0 or self.move_direction == 2:
            self.turn_right()

    def key_turn_left(self, event):
        if self.move_direction == 0 or self.move_direction == 2:
            self.turn_left()

    def move(self):
        if not self.if_game_finished:
            if self.move_direction == 0:
                self.go_up()
            elif self.move_direction == 1:
                self.turn_right()
            elif self.move_direction == 2:
                self.go_down()
            else:
                self.turn_left()
        else:
            self.if_game_finished = False
            return False

    def if_win(self):
        if (len(self.position) + len(self.obstacle_position)) == self.available_game_board_size:
            return True

    def reset(self):
        if not self.if_game_finished and not self.if_win():
            if not self.pause:
                self.pixel.delete("all")
                if not super().snake_cross() and not self.obstacle_colision():
                    super().create_game_border()
                    self.snake_ate_food()
                    super().create_obstacles()
                    super().create_food()
                else:
                    self.game_lost = True
                    messagebox.showinfo("Game over", "You lost, try again!")
        elif self.if_win():
            messagebox.showinfo("You win", "You win, congratulations!")
            self.game_won = True

    def restart(self):
        self.pixel.delete("all")
        self.move_direction = random.randint(0, 1)
        self.food_position = []
        super().generate_food_list()
        if not self.if_file:
            self.obstacle_position = []
            self.position = [(self.width / 2, self.height / 2), (self.width / 2, self.height / 2 + 10), (self.width / 2, self.height / 2 + 20)]
            super().generate_obstacle_list()
        self.if_game_finished = False

    def quit(self):
        self.master.quit()
