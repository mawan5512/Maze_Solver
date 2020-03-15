import pytest
from maze_solver import find_shortest_path, make_mazes, parse_maze_string, decode_room

class TestDecodeRoom(object):

    @pytest.mark.parametrize("function_args, error_message", [
        (([]), r"room_value is not an int!"),
        ((1.0), r"room_value is not an int!"),
        ((()), r"room_value is not an int!"),
        (({}), r"room_value is not an int!"),
        ((None), r"room_value is not an int!"),
        ((set([])), r"room_value is not an int!"),
        ((''), r"room_value is not an int!"),
        ((True), r"room_value is not an int!"),
        ((False), r"room_value is not an int!"),
        ((128), r"room_value is not in range!"),
        ((-1), r"room_value is not in range!")
    ])
    def test_decode_room_parameters_are_invalid(self, function_args, error_message):
        with pytest.raises(Exception, match=error_message):
            room_value = function_args
            decode_room(room_value)

    @pytest.mark.parametrize("function_args, expected_result", [
        ((2), {"mine": False, "start": False, "end": False, "up": False, "down": False, "left": False, "right": True}),
        ((68), {"mine": True, "start": False, "end": False, "up": False, "down": True, "left": False, "right": False}),
        ((17), {"mine": False, "start": True, "end": False, "up": True, "down": False, "left": False, "right": False}),
        ((40), {"mine": False, "start": False, "end": True, "up": False, "down": False, "left": True, "right": False})

    ])
    def test_decode_room_parameters_are_valid(self, function_args, expected_result):
        room_value = function_args
        decoded_room = decode_room(room_value)
        assert decoded_room == expected_result

class TestParseMazeString(object):

    @pytest.mark.parametrize("function_args, error_message", [
        (([]), r"maze_string is not a string!"),
        ((1.0), r"maze_string is not a string!"),
        ((()), r"maze_string is not a string!"),
        (({}), r"maze_string is not a string!"),
        ((None), r"maze_string is not a string!"),
        ((set([])), r"maze_string is not a string!"),
        ((1), r"maze_string is not a string!"),
        ((True), r"maze_string is not a string!"),
        ((False), r"maze_string is not a string!"),
        ((''), r"maze_string is not valid!"),
        (("(3,3)-[34,14,12,6,77,5,1,1,9]"), r"no start node was provided!"),
        (("(3,3)-[30,14,12,6,77,5,1,19,9]"), r"no end node was provided!")
    ])
    def test_parse_maze_string_parameters_are_invalid(self, function_args, error_message):
        with pytest.raises(Exception, match=error_message):
            maze_string = function_args
            parse_maze_string(maze_string)
    
    @pytest.mark.parametrize("function_args, expected_result", [
        (("(3,3)-[34,14,12,6,77,5,1,19,9]"), {
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': True, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        })
    ])
    def test_parse_maze_parameters_are_valid(self, function_args, expected_result):
        maze_string = function_args
        parsed_maze = parse_maze_string(maze_string)
        assert parsed_maze == expected_result

class TestMakeMazes(object):

    @pytest.mark.parametrize("function_args, error_message", [
        (([]), r"maze_file_path is not a string!"),
        ((1.0), r"maze_file_path is not a string!"),
        ((()), r"maze_file_path is not a string!"),
        (({}), r"maze_file_path is not a string!"),
        ((None), r"maze_file_path is not a string!"),
        ((set([])), r"maze_file_path is not a string!"),
        ((1), r"maze_file_path is not a string!"),
        ((True), r"maze_file_path is not a string!"),
        ((False), r"maze_file_path is not a string!"),
        ((""), r"No such file or directory: ''")
    ])
    def test_make_mazes_parameters_are_invalid(self, function_args, error_message):
        with pytest.raises(Exception, match=error_message):
            maze_file = function_args
            make_mazes(maze_file)
    
    @pytest.mark.parametrize("function_args, expected_result", [
        (("test_mazes.txt"), [{
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': True, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        },{
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': True, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        },{
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': False, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        }])
    ])
    def test_make_mazes_string_parameters_are_valid(self, function_args, expected_result):
        maze_file = function_args
        mazes = make_mazes(maze_file)
        assert mazes == expected_result

class TestFindShortestPath(object):
    
    @pytest.mark.parametrize("function_args, error_message", [
        (([]), r"maze is not a dict!"),
        ((1.0), r"maze is not a dict!"),
        ((()), r"maze is not a dict!"),
        ((None), r"maze is not a dict!"),
        ((set([])), r"maze is not a dict!"),
        ((1), r"maze is not a dict!"),
        ((True), r"maze is not a dict!"),
        ((False), r"maze is not a dict!"),
        ((""), r"maze is not a dict!")
    ])
    def test_find_shortest_path_parameters_are_invalid(self, function_args, error_message):
        with pytest.raises(Exception, match=error_message):
            maze = function_args
            find_shortest_path(maze)

    @pytest.mark.parametrize("function_args, expected_result", [
        (({
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': True, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        }), ['up', 'up', 'left']),
        (({
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': True, 'right': False, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        }), ['N/A']),
        (({
            (1,1): {'up': False, 'right': True, 'down': False, 'left': False, 'start': False, 'end': True, 'mine': False},
            (1,2): {'up': False, 'right': True, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (1,3): {'up': False, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': False},
            (2,1): {'up': False, 'right': True, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (2,2): {'up': True, 'right': False, 'down': True, 'left': True, 'start': False, 'end': False, 'mine': True},
            (2,3): {'up': True, 'right': False, 'down': True, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,1): {'up': True, 'right': False, 'down': False, 'left': False, 'start': False, 'end': False, 'mine': False},
            (3,2): {'up': False, 'right': True, 'down': False, 'left': False, 'start': True, 'end': False, 'mine': False},
            (3,3): {'up': True, 'right': False, 'down': False, 'left': True, 'start': False, 'end': False, 'mine': False},
            "start": (3,2)
        }), ['right', 'up', 'up', 'left', 'left'])
    ])
    def test_find_shortest_path_parameters_are_valid(self, function_args, expected_result):
        maze = function_args
        shortest_path = find_shortest_path(maze)
        assert shortest_path == expected_result