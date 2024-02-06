"""Custom module for rendering the game window"""
from window import Window, Point, Line
from cell import Cell
 

def main():
    """main function for running all functions"""
    win = Window(1000, 800)
    # for i in range(50, 600, 50):
    #     new_cell = Cell(i, i + 50, win)
    #     if i % 100 == 0:
    #         new_cell.has_bottom_wall = False
    #         new_cell.has_right_wall = False
    #     new_cell.draw("black")
    # win.draw_line(new_line,"blue")
    cell_1 = Cell(250, 300, win)
    cell_2 = Cell(350, 400, win)
    cell_1.draw("black")
    cell_2.draw("blue")
    cell_1.draw_move(cell_2, undo=True)
    win.wait_for_close()

main()
