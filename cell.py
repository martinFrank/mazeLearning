class Cell:
    door_north = 0
    door_east = 0
    door_west = 0
    door_south = 0
    visited = 0
    x_pos = 0
    y_pos = 0

    def __init__(self, xp, yp):
        self.x_pos = xp
        self.y_pos = yp

    def top_row(self):
        door = "###"
        if self.door_north == 1:
            door = "   "
        return "#" + door + "#"

    def mid_row(self):
        left_door = "#"
        if self.door_west == 1:
            left_door = " "
        right_door = "#"
        if self.door_east == 1:
            right_door = " "
        return left_door + "   " + right_door

    def bot_row(self):
        door = "###"
        if self.door_south == 1:
            door = "   "
        return "#" + door + "#"

