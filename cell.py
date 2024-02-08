from window import Point, Line


class Cell:
    """This class will create a box that lives on the windows grid. It takes the X and Y coordinates of the top-left point"""
    def __init__(self,x1,y1,x2,y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.center_x = self.__x1 + (self.__x2 - self.__x1) / 2
        self.center_y = self.__y1 + (self.__y2 - self.__y1) / 2
        self.__win = window


    def get_x1(self):
        """Getter method for the x1 coordinate"""
        return self.__x1
    def get_y1(self):
        """Getter method for the y1 coordinate"""
        return self.__y1
    def draw(self, color):
        """Draw the walls of the cell"""
        top_left_point = Point(self.__x1, self.__y1)
        top_right_point = Point(self.__x2, self.__y1)
        bottom_left_point = Point(self.__x1, self.__y2)
        bottom_right_point = Point(self.__x2, self.__y2)
        if self.has_left_wall:
            left_line = Line(top_left_point, bottom_left_point )
            self.__win.draw_line(left_line, color)
        if self.has_right_wall:
            right_line = Line(top_right_point, bottom_right_point)
            self.__win.draw_line(right_line, color)
        if self.has_top_wall:
            top_line = Line(top_left_point,top_right_point)
            self.__win.draw_line(top_line, color)
        if self.has_bottom_wall:
            bottom_line = Line(bottom_left_point, bottom_right_point)
            self.__win.draw_line(bottom_line, color)
    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "red"
        else:
            line_color = "grey"
        center_point = Point(self.center_x, self.center_y)
        to_cell_center = Point(to_cell.center_x, to_cell.center_y)
        if to_cell.get_y1() != self.__y1:
            turn_point = Point(to_cell.center_x, self.center_y)
            self.__win.draw_line(Line(center_point, turn_point), line_color)
            self.__win.draw_line(Line(turn_point, to_cell_center), line_color)

        if to_cell.get_y1() == self.__y1:  # Cells are in the same row
            self.__win.draw_line(Line(center_point,to_cell_center), line_color)
