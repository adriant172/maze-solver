from window import Point, Line


class Cell:
    """This class will create a box that lives on the windows grid"""
    def __init__(self,x,y, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x
        self.__x2 = y
        self.__y1 = y
        self.__y2 = x
        self.__win = window
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