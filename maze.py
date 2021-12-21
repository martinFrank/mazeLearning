import cell
import random


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

    NEIGHBOR_OFFSETS = (
        (0, -1),  # north
        (1, 0),   # east
        (0, 1),   # south
        (-1, 0),  # west
    )

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}

        for dy in range(0, height):
            for dx in range(0, width):
                self.cells[dx, dy] = cell.Cell(dx, dy)

    # see https://en.wikipedia.org/wiki/Maze_generation_algorithm
    def back_tracker(self):
        stack = []
        current = self.cells[random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
        current.visited = True
        stack.append(current)
        while stack:
            current = stack.pop()
            unvisited = self.unvisited_neighbors(current)
            if unvisited:
                stack.append(current)
                random_index = random.randint(0, len(unvisited) - 1)
                chosen = unvisited[random_index]
                carve(chosen, current)
                current = chosen
                current.visited = True
                stack.append(current)

    def unvisited_neighbors(self, current):
        x, y = (current.x_pos, current.y_pos)
        neighbors = []
        for dx, dy in self.NEIGHBOR_OFFSETS:
            pos = x + dx, y + dy
            if pos in self.cells:
                current = self.cells[pos]
                if not current.visited:
                    neighbors.append(current)
        return neighbors

    def print_maze(self):
        for dy in range(0, self.height):
            top_row = ""
            mid_row = ""
            bot_row = ""
            for dx in range(0, self.width):
                top_row = top_row + self.cells[dx, dy].top_row()
                mid_row = mid_row + self.cells[dx, dy].mid_row()
                bot_row = bot_row + self.cells[dx, dy].bot_row()
            print(top_row)
            print(mid_row)
            print(bot_row)
