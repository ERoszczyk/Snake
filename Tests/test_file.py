import pytest
from ReadFromFile import ReadFromFile
from Errors import NotTxtFileError, TooManyObstaclesError, NoSnakeError, GameBoardSizeError, InvalidGameBoardError
from tkinter import Tk


def test_txt_error():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "Attributes.py"

    with pytest.raises(NotTxtFileError):
        assert test.read_game_board_from_file()


def test_it_txt():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "txt.txt"
    test.if_txt()
    assert True


def test_too_many_obstacles():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_too_many_obstacles.txt"
    with pytest.raises(TooManyObstaclesError):
        assert test.read_game_board_from_file()


def test_no_snake():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_no_snake.txt"
    with pytest.raises(NoSnakeError):
        assert test.read_game_board_from_file()


def test_wrong_game_board_size():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_wrong_size.txt"
    with pytest.raises(GameBoardSizeError):
        assert test.read_game_board_from_file()


def test_string_as_game_board_size():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_string_in_first_line.txt"
    with pytest.raises(GameBoardSizeError):
        assert test.read_game_board_from_file()


def test_no_board_size():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_without_game_board_size.txt"
    with pytest.raises(GameBoardSizeError):
        assert test.read_game_board_from_file()


def test_bigger_value_than_game_board_size():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_different_value_than_size.txt"
    with pytest.raises(InvalidGameBoardError):
        assert test.read_game_board_from_file()


def test_smaller_value_than_game_board_size():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_different_value_than_size2.txt"
    with pytest.raises(InvalidGameBoardError):
        assert test.read_game_board_from_file()


def test_no_boarden():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_no_boarden.txt"
    with pytest.raises(InvalidGameBoardError):
        assert test.read_game_board_from_file()


def test_boarden_inside_game_board():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_boarden_inside_game_board.txt"
    with pytest.raises(InvalidGameBoardError):
        assert test.read_game_board_from_file()


def test_boarden_inside_game_board2():
    window = Tk()
    test = ReadFromFile(window, 300, 300, 5, 3, 150)
    test.user_input = "test_boarden_inside_game_board2.txt"
    with pytest.raises(InvalidGameBoardError):
        assert test.read_game_board_from_file()
