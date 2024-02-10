from cell import Cell
import time

class Maze:
    """This class will create a 2 dimensional grid of cells"""
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
    def _create_cells(self):
        for _ in range(self._num_cols):
            new_col = []
            for _ in range(self._num_rows):
                new_col.append(Cell(self._win))
            self._cells.append(new_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        current_cell = self._cells[i][j]
        cell_x = self._x1 + j * self._cell_size_x
        cell_y = self._y1 + i * self._cell_size_y
        current_cell.draw(cell_x,cell_y, cell_x + self._cell_size_x, cell_y + self._cell_size_y, "black")
        self._animate()
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        self._draw_cell(0,0)
        # first_cell.draw(
        #     first_cell._x1,
        #     first_cell._y1,
        #     first_cell._x2,
        #     first_cell._y2,
        #     "black"
        # )
        last_cell.has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        # last_cell.draw(
        #     last_cell._x1,
        #     last_cell._y1,
        #     last_cell._x2,
        #     last_cell._y2,
        #     "black"
        # )






