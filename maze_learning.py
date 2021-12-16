import maze


def main():
    print("main...")
    my_maze = maze.Maze(64, 64)
    my_maze.back_tracker()
    my_maze.print_maze()


if __name__ == "__main__":
    main()
