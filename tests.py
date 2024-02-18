import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_2(self):
        num_cols = 20
        num_rows = 15
        m2 = Maze(0,0,num_rows,num_cols,25,25)
        self.assertEqual(
            len(m2._cells),
            num_cols
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )
    def test_maze_break_walls(self):
        num_cols = 20
        num_rows = 10
        m3 = Maze(0,0,num_rows,num_cols,15,15)
        m3._break_entrance_and_exit()
        self.assertEqual(
            m3._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m3._cells[-1][-1].has_right_wall,
            False,
        )
    def test_maze_reset_visited(self):
        num_cols = 20
        num_rows = 10
        m4 = Maze(0,0,num_rows,num_cols,15,15)
        for i, col in enumerate(m4._cells):
            for j, cell in enumerate(m4._cells[i]):
                self.assertEqual(
                    m4._cells[i][j].visited,
                    False,
                )

        
if __name__ == "__main__":
    unittest.main()
