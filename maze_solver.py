from collections import deque 

def decode_room(room_value):
    """
    Function to take encoded room value and parse it into a room object then return it
    """
    try:
        if not isinstance(room_value, int) or isinstance(room_value, bool):
            raise Exception("room_value is not an int!")
        if not 0 <= room_value <= 127:
            raise Exception("room_value is not in range!")
        feature_codes = {
            "up": 1,
            "right": 2,
            "down": 4,
            "left": 8,
            "start": 16,
            "end": 32,
            "mine": 64
        }
        room_object = {}

        for key, val in feature_codes.items():
            room_object[key] = False
            if room_value & val != 0:
                room_object[key] = True
        return room_object
    except Exception as e:
        raise e

def parse_maze_string(maze_string):
    """
    Function that parses a maze string into a maze object. 
    The maze object is a Dict with keys being the room IDs.
    Room IDs are tuple as such (i, j) representing room in row i and column j
    """
    try:
        if not isinstance(maze_string, str):
            raise Exception("maze_string is not a string!")
        maze_info = maze_string.split("-")
        if len(maze_info) != 2:
            raise Exception("maze_string is not valid!")
        try:
            maze_dimensions = eval(maze_info[0])
            maze_rooms = eval(maze_info[1])
        except Exception:
            raise Exception("maze_string is not valid!")
        maze_object = {}
        start_node = None
        end_node = None
        for i in range(1, int(maze_dimensions[0]) + 1):
            for j in range(1, int(maze_dimensions[1]) + 1):
                maze_object[(i, j)] = decode_room(int(maze_rooms[((i - 1) * int(maze_dimensions[1])) + j - 1]))
                if maze_object[(i, j)]["start"]:
                    start_node = (i,j)

                if maze_object[(i, j)]["end"]:
                    end_node = (i,j)

        if not start_node:
            raise Exception("no start node was provided!")

        if not end_node:
            raise Exception("no end node was provided!")

        maze_object["start"] = start_node

        return maze_object
    except Exception as e:
        raise e

def make_mazes(maze_file_path):
    """
    Function which takes the maze file with many mazes and parses them into an an array of maze_objects.
    """
    try:
        if not isinstance(maze_file_path, str):
            raise Exception("maze_file_path is not a string!")
        mazes = []
        with open(maze_file_path, "r") as f:
            for idx, maze_string in enumerate(f):
                try:
                    print("Loading in maze #{}:\n{}".format(idx + 1, maze_string))
                    mazes.append(parse_maze_string(maze_string))
                    print("Maze Loaded!\n")
                except Exception as e:
                    print("There was an error loading maze: {}\n".format(e))

        return mazes
    except Exception as e:
        raise e

def find_shortest_path(maze):
    """
    Function that searches for the shortest path in a given maze.
    It is using an enhanced version of an ordinary breadth first search.
    If a path cannot be found it will be printed out to the user.
    """
    try:
        lives = 3
        if not isinstance(maze, dict):
            raise Exception("maze is not a dict!")
        queue = deque()
        start_node = maze["start"]
        path = []
        visited = set([])
        q_object = {
            "node": start_node,
            "lives": lives,
            "path": path,
            "visited": visited
        }
        queue.append(q_object)
        while queue:
            current_queue_object = queue.popleft()
            current_node_object = maze[current_queue_object["node"]]

            if current_queue_object["node"] in current_queue_object["visited"]:
                continue
            else:
                current_queue_object["visited"].add(current_queue_object["node"])
            if current_node_object["mine"]:
                current_queue_object["lives"] -= 1
            if current_queue_object["lives"] <= 0:
                continue
            if current_node_object["end"]:
                path = current_queue_object["path"]
                break

            if current_node_object["up"]:
                new_path = list(current_queue_object["path"])
                new_path.append('up')
                queue.append({
                    "node": (int(current_queue_object["node"][0]) - 1, int(current_queue_object["node"][1])),
                    "lives": int(current_queue_object["lives"]),
                    "path": new_path,
                    "visited": set(current_queue_object["visited"])
                })

            if current_node_object["down"]:
                new_path = list(current_queue_object["path"])
                new_path.append('down')
                queue.append({
                    "node": (int(current_queue_object["node"][0]) + 1, int(current_queue_object["node"][1])),
                    "lives": int(current_queue_object["lives"]),
                    "path": new_path,
                    "visited": set(current_queue_object["visited"])
                })
                
            if current_node_object["left"]:
                new_path = list(current_queue_object["path"])
                new_path.append('left')
                queue.append({
                    "node": (int(current_queue_object["node"][0]), int(current_queue_object["node"][1]) - 1),
                    "lives": int(current_queue_object["lives"]),
                    "path": new_path,
                    "visited": set(current_queue_object["visited"])
                })

            if current_node_object["right"]:
                new_path = list(current_queue_object["path"])
                new_path.append('right')
                queue.append({
                    "node": (int(current_queue_object["node"][0]), int(current_queue_object["node"][1]) + 1),
                    "lives": int(current_queue_object["lives"]),
                    "path": new_path,
                    "visited": set(current_queue_object["visited"])
                })

        if not path:
            path = ["N/A"]
            print("We couldn't find a path through in the map\n")
        else:
            print("We found a path through in the map with {} lives: {}\n".format(current_queue_object["lives"], path))

        return path

    except Exception as e:
        raise e

def main():
    """
    Main function to run the maze_solver.py
    """
    file_path = "mazes.txt"
    mazes = make_mazes(file_path)
    shortest_paths = []
    for idx, maze in enumerate(mazes):
        print("Trying to solve maze #{}:\n".format(idx + 1))
        shortest_paths.append(find_shortest_path(maze))   
    print("Output Answer:\n{}".format(shortest_paths))

if __name__ == '__main__':
    main()
