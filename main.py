"""Custom module for rendering the game window"""
from window import Window
from maze import Maze
 

def main():
    """main function for running all functions"""
    win = Window(1000, 1000)

    x1 = 50
    y1 = 50
    num_rows = 10
    num_cols = 10
    cell_size_x = 50
    cell_size_y = 50
    maze = Maze(x1, y1, num_rows,num_cols,cell_size_x,cell_size_y, win)
    maze.solve()
    win.wait_for_close()

main()
