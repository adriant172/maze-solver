"""Custom module for rendering the game window"""

from window import Window, Point, Line


def main():
    """main function for running all functions"""
    win = Window(800, 600)
    point_a = Point(450,370)
    point_b = Point(180, 600)
    new_line = Line(point_a,point_b)
    win.draw_line(new_line,"blue")
    win.wait_for_close()

main()
