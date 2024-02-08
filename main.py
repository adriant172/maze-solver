"""Custom module for rendering the game window"""
from window import Window, Point, Line
from maze import Maze
from cell import Cell
 

def main():
    """main function for running all functions"""
    win = Window(1000, 1000)

    x1 = 50
    y1 = 50
    num_rows = 5
    num_cols = 5
    cell_size_x = 50
    cell_size_y = 50
    maze = Maze(x1, y1, num_rows,num_cols,cell_size_x,cell_size_y, win)
    
    # cell_1 = Cell(win)
    # cell_1.has_right_wall = False
    # cell_1.has_left_wall = False
    # cell_2 = Cell(win)
    # cell_2.has_bottom_wall = False
    # # cell_3 = Cell(800,700,900,800, win)
    # cell_1.draw(750,750,800,800,"black")
    # cell_2.draw(650,650,700,700,"blue")
   
    # cell_1.draw_move(cell_2, undo=True)
    win.wait_for_close()

main()
