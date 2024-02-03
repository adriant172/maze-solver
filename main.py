"""Custom module for rendering the game window"""

from window import Window


def main():
    """main function for running all functions"""
    win = Window(800, 600)
    win.wait_for_close()


main()
