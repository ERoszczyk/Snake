from tkinter import Button, Label, Radiobutton, IntVar, Spinbox, Menu, PhotoImage, messagebox
from Game import Game


class StartWindow(Game):
    """
    This class contains menu and its modes.
    It is responsible for the appropriate response to user actions.
    """
    def __init__(self, master):
        super().__init__(master)
        self.start_master = master

        master.title("Snake")
        master.iconbitmap(r'snake_icon.ico')
        master.geometry("300x300")

        self.start_menu_mode()

    def clean_window(self):
        self.all_widgets = []
        for widget in self.start_master.children.values():
            self.all_widgets.append(widget)
        for widget in self.all_widgets:
            widget.destroy()

    def start_menu_mode(self):
        self.clean_window()
        self.if_file = False
        self.image = PhotoImage(file="snake_icon.png")
        self.image_label = Label(self.start_master, image=self.image)
        self.play_game_button = Button(self.start_master, text="Play a game", width=20, command=self.select_game_parametrs, fg='White', bg='#2D92CC', borderwidth=4)
        self.open_game_from_file_button = Button(self.start_master, text="Load game board from file", width=20, command=self.load_game_board_from_file, fg='White', bg='#2D92CC', borderwidth=4)
        self.exit_button = Button(self.start_master, text="Exit", width=20, command=self.menu_quit, fg='White', bg='#2D92CC', borderwidth=4)
        self.play_game_button.place(x=75, y=165)
        self.open_game_from_file_button.place(x=75, y=215)
        self.exit_button.place(x=75, y=265)
        self.image_label.place(x=65, y=0)

    def create_menu(self):
        self.menubar = Menu(self.master)
        self.menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Menu", menu=self.menu)
        self.menu.add_command(label="Pause", command=self.game_pause, state='disabled')
        self.menu.add_command(label="Resume", command=self.resume, state='disabled')
        self.menu.add_command(label="Restart", command=self.game_restart, state='disabled')
        self.menu.add_command(label="Main menu", command=self.back_to_the_main_menu)
        self.menu.add_command(label="Open game from file", command=self.open_from_file)
        self.menu.add_command(label="Exit", command=self.game_quit)

        self.master.config(menu=self.menubar)

    def undisabled_command(self, command):
        self.menu.entryconfig(command, state='normal')

    def disabled_command(self, command):
        self.menu.entryconfig(command, state='disabled')

    def menu_play_mode(self):
        self.disabled_command(1)
        self.undisabled_command(0)
        self.undisabled_command(2)
        self.undisabled_command(4)
        self.undisabled_command(5)

    def game_pause(self):
        self.snake.pause = True
        self.disabled_command(0)
        self.undisabled_command(1)
        self.undisabled_command(2)
        self.undisabled_command(4)
        self.undisabled_command(5)

    def resume(self):
        self.snake.pause = False
        self.menu_play_mode()

    def game_restart(self):
        self.game_pause()
        self.restart_box = messagebox.askquestion("Restart game", "Are you sure you want to restart the game?")
        if self.restart_box == "yes":
            if self.if_file:
                self.reload_starting_position()
            self.snake.if_game_finished = True
            self.snake.restart()
            self.snake.pause = False
            self.menu_play_mode()
        else:
            self.resume()

    def main_menu(self):
        self.snake.if_game_finished = True
        self.start_menu_mode()
        self.start_master.geometry("300x300")

    def back_to_the_main_menu(self):
        self.game_pause()
        self.end_game_box = messagebox.askquestion("Go back to the main menu", "Are you sure you want to quit the game and return to the main menu?")
        if self.end_game_box == "yes":
            self.main_menu()
        else:
            self.resume()

    def reload_starting_position(self):
        super().load_snake_from_file()
        self.snake.position = self.position

    def open_from_file(self):
        self.game_pause()
        self.end_game_box = messagebox.askquestion("Open game board from file", "Are you sure you want to quit the game and open game board from file?")
        if self.end_game_box == "yes":
            for command in range(6):
                self.disabled_command(command)
            self.snake.if_game_finished = True
            self.start_menu_mode()
            self.start_master.geometry("300x300")
            self.load_game_board_from_file()
        else:
            self.resume()

    def game_start(self):
        self.clean_window()
        if not self.if_file:
            self.width = self.window_size.get()
            self.height = self.window_size.get()
            self.obstacle_number = self.number_of_obstacles.get()
            self.position = [(self.width / 2, self.height / 2), (self.width / 2, self.height / 2 + 10), (self.width / 2, self.height / 2 + 20)]
        self.food_amount = self.amount_of_food.get()
        self.snake_speed = self.selected_snake_speed.get()
        self.snake = Game(self.start_master, self.width, self.height, self.food_amount, self.obstacle_number, self.snake_speed)
        self.snake.position = self.position
        self.create_menu()
        self.menu_play_mode()
        self.snake.if_file = self.if_file
        self.snake.obstacle_position = self.obstacle_position
        self.snake_move()

    def snake_move(self):
        if not self.snake.if_game_finished:
            self.snake.move()
            if not self.snake.game_lost and not self.snake.game_won:
                self.snake.master.after(self.snake_speed, self.snake_move)
            else:
                self.main_menu()
        else:
            self.snake.if_game_finished = False

    def load_game_board_from_file(self):
        super().ask_for_file()
        if self.user_input != "":
            super().read_game_board_from_file()
            if self.if_file:
                self.width = self.x_coordinate * 10
                self.height = self.y_coordinate * 10
                self.obstacle_number = len(self.obstacle_position)
                self.game_board_from_file_parametrs()
                self.snake_speed = self.selected_snake_speed.get()
                self.buttons_while_choosing_parametrs()

    def select_game_parametrs(self):
        self.clean_window()
        self.select_window_size()
        self.select_food_amount()
        self.select_obstacles_number()
        self.select_snake_speed(150)
        self.buttons_while_choosing_parametrs()

    def game_board_from_file_parametrs(self):
        self.clean_window()
        self.select_food_amount()
        self.select_snake_speed(10)

    def select_window_size(self):
        self.window_size = IntVar()
        self.size_select_label = Label(self.start_master, text="Select a board size:")
        self.size30_button = Radiobutton(self.start_master, variable=self.window_size, value=300, text="30x30")
        self.size40_button = Radiobutton(self.start_master, variable=self.window_size, value=400, text="40x40")
        self.size50_button = Radiobutton(self.start_master, variable=self.window_size, value=500, text="50x50")
        self.size60_button = Radiobutton(self.start_master, variable=self.window_size, value=600, text="60x60")
        self.window_size.set(300)
        self.size_select_label.place(x=10, y=10)
        self.size30_button.place(x=20, y=30)
        self.size40_button.place(x=120, y=30)
        self.size50_button.place(x=20, y=50)
        self.size60_button.place(x=120, y=50)

    def select_food_amount(self):
        self.food_choice_label = Label(self.start_master, text="Select food amount:")
        self.amount_of_food = IntVar()
        self.food_amount_choice = Spinbox(self.start_master, from_=1, to=10, width=10, textvariable=self.amount_of_food, state="readonly")
        self.food_choice_label.place(x=10, y=85)
        self.food_amount_choice.place(x=200, y=90)

    def select_obstacles_number(self):
        self.obstacles_choice_label = Label(self.start_master, text="Select number of obstacles:")
        self.number_of_obstacles = IntVar()
        self.obstacles_number_choice = Spinbox(self.start_master, from_=0, to=10, width=10, textvariable=self.number_of_obstacles, state="readonly")
        self.obstacles_choice_label.place(x=10, y=115)
        self.obstacles_number_choice.place(x=200, y=120)

    def select_snake_speed(self, y):
        self.selected_snake_speed = IntVar()
        self.select_snake_speed_label = Label(self.start_master, text="Select snake speed:")
        self.speed100_button = Radiobutton(self.start_master, variable=self.selected_snake_speed, value=100, text="Very fast")
        self.speed130_button = Radiobutton(self.start_master, variable=self.selected_snake_speed, value=130, text="Fast")
        self.speed175_button = Radiobutton(self.start_master, variable=self.selected_snake_speed, value=175, text="Slow")
        self.speed200_button = Radiobutton(self.start_master, variable=self.selected_snake_speed, value=200, text="Very slow")
        self.selected_snake_speed.set(200)
        self.select_snake_speed_label.place(x=10, y=y)
        self.speed100_button.place(x=120, y=y + 40)
        self.speed130_button.place(x=20, y=y + 40)
        self.speed175_button.place(x=120, y=y + 20)
        self.speed200_button.place(x=20, y=y + 20)

    def buttons_while_choosing_parametrs(self):
        self.start_button = Button(self.start_master, text="Start", width=10, command=self.game_start, fg='White', bg='#2D92CC', borderwidth=4)
        self.start_button.place(x=180, y=250)
        self.back_button = Button(self.start_master, text="Back", width=10, command=self.start_menu_mode, fg='White', bg='#2D92CC', borderwidth=4)
        self.back_button.place(x=40, y=250)

    def menu_quit(self):
        self.quit_box = messagebox.askquestion("Exit game", "Are you sure you want to quit the game?")
        if self.quit_box == "yes":
            self.start_master.quit()

    def game_quit(self):
        self.snake.pause = True
        self.quit_box = messagebox.askquestion("Exit game", "Are you sure you want to quit the game?")
        if self.quit_box == "yes":
            self.start_master.quit()
        else:
            self.resume()
