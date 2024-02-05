"""Custom module for rendering the game window"""
from window import Window, Point, Line
from cell import Cell
 

def main():
    """main function for running all functions"""
    win = Window(800, 600)
    for i in range(50, 600, 50):
        new_cell = Cell(i, i + 50, win)
        if i % 100 == 0:
            new_cell.has_bottom_wall = False
            new_cell.has_right_wall = False
        new_cell.draw("black")
    # win.draw_line(new_line,"blue")
    win.wait_for_close()

main()
