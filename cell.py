class Cell:
    door_north = False
    door_east = False
    door_west = False
    door_south = False
    visited = False
    x_pos = 0
    y_pos = 0

    def __init__(self, xp, yp):
        self.x_pos = xp
        self.y_pos = yp

    def top_row(self):
        door = "###"
        if self.door_north:
            door = "   "
        return "#" + door + "#"

    def mid_row(self):
        left_door = "#"
        if self.door_west:
            left_door = " "
        right_door = "#"
        if self.door_east:
            right_door = " "
        return left_door + "   " + right_door

    def bot_row(self):
        door = "###"
        if self.door_south:
            door = "   "
        return "#" + door + "#"

