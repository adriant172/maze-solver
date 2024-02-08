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
            win,
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
        current_cell = self._cells[i][j]
        cell_x = self._x1 + j * self._cell_size_x
        cell_y = self._y1 + i * self._cell_size_y
        current_cell.draw(cell_x,cell_y, cell_x + self._cell_size_x, cell_y + self._cell_size_y, "black")
        self._animate()
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)






