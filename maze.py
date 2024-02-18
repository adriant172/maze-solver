import time
import random
from cell import Cell


class Maze:
    """This class will create a 2 dimensional grid of cells"""

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        cell_x = self._x1 + i * self._cell_size_x
        cell_y = self._y1 + j * self._cell_size_y
        current_cell.draw(
            cell_x,
            cell_y,
            cell_x + self._cell_size_x,
            cell_y + self._cell_size_y,
            "black",
        )
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        self._draw_cell(0, 0)
        last_cell.has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            # left
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            # right
            if i < self._num_cols - 1:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            # up
            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            # down
            if j < self._num_rows - 1:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            if not to_visit:
                self._draw_cell(i, j)
                return
            next_i, next_j = to_visit[random.randrange(len(to_visit))]
            next_cell = self._cells[next_i][next_j]

            if next_i > i:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            if next_i < i:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            if next_j > j:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            if next_j < j:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i, col in enumerate(self._cells):
            for j, cell in enumerate(self._cells[i]):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == (self._num_cols - 1 ) and j == (self._num_rows - 1):
            return True
        # left
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i][j].has_left_wall
        ):
            print(f"Going left to cell at {i - 1}, {j}")
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            result = self._solve_r(i - 1, j)
            if result:
                return result
            self._cells[i - 1][j].draw_move(self._cells[i][j], undo=True)
        # right
        if (
            i < self._num_cols - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_right_wall
        ):
            print(f"Going right to cell at {i + 1}, {j} ")
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            result = self._solve_r(i + 1, j)
            if result:
                return result
            self._cells[i + 1][j].draw_move(self._cells[i][j], undo=True)
        # top
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_top_wall
        ):
            print(f"Going up to cell at {i}, {j - 1}")
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            result = self._solve_r(i, j - 1)
            if result:
                return result
            self._cells[i][j - 1].draw_move(self._cells[i][j], undo=True)    
        # bottom
        if (
            j < self._num_rows - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            print(f"Going down to cell at {i }, {j + 1}")
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            result = self._solve_r(i, j + 1)
            if result:
                return result
            self._cells[i][j + 1].draw_move(self._cells[i][j], undo=True)

        return False