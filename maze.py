import cell
import random


def pop(stack):
    item = stack[len(stack) - 1]
    del stack[len(stack) - 1]
    return item


def push(item, stack):
    size = len(stack)
    stack[size] = item


def add_if_unvisited(maze, pos, target):
    if pos in maze:
        current = maze[pos]
        if not current.visited:
            target.append(current)


def carve(from_cell, to_cell):
    if to_cell.x_pos - from_cell.x_pos == 1:
        from_cell.door_east = True
        to_cell.door_west = True
    if to_cell.x_pos - from_cell.x_pos == -1:
        from_cell.door_west = True
        to_cell.door_east = True
    if to_cell.y_pos - from_cell.y_pos == -1:
        from_cell.door_north = True
        to_cell.door_south = True
    if to_cell.y_pos - from_cell.y_pos == 1:
        from_cell.door_south = True
        to_cell.door_north = True


class Maze:
    width = 0
    height = 0
    cells = {}

    def __init__(self, width, height):
        self.width = width
        self.height = height

        for dy in range(0, height):
            for dx in range(0, width):
                self.cells[complex(dx, dy)] = cell.Cell(dx, dy)

    # see https://en.wikipedia.org/wiki/Maze_generation_algorithm
    def back_tracker(self):
        stack = {}
        current = self.cells[complex(random.randint(0, self.width - 1), random.randint(0, self.height - 1))]
        current.visited = True
        push(current, stack)
        while len(stack) > 0:
            current = pop(stack)
            unvisited = self.list_unvisited(current)
            if len(unvisited) > 0:
                push(current, stack)
                random_index = random.randint(0, len(unvisited) - 1)
                chosen = unvisited[random_index]
                carve(chosen, current)
                current = chosen
                current.visited = True
                push(current, stack)

    def list_unvisited(self, current):
        pos_north = complex(current.x_pos, current.y_pos - 1)
        pos_east = complex(current.x_pos + 1, current.y_pos)
        pos_south = complex(current.x_pos, current.y_pos + 1)
        pos_west = complex(current.x_pos - 1, current.y_pos)

        neighbors = []
        add_if_unvisited(self.cells, pos_north, neighbors)
        add_if_unvisited(self.cells, pos_east, neighbors)
        add_if_unvisited(self.cells, pos_south, neighbors)
        add_if_unvisited(self.cells, pos_west, neighbors)
        return neighbors

    def print_maze(self):

        for dy in range(0, self.height):
            top_row = ""
            mid_row = ""
            bot_row = ""
            for dx in range(0, self.width):
                top_row = top_row + self.cells[complex(dx, dy)].top_row()
                mid_row = mid_row + self.cells[complex(dx, dy)].mid_row()
                bot_row = bot_row + self.cells[complex(dx, dy)].bot_row()
            print(top_row)
            print(mid_row)
            print(bot_row)
