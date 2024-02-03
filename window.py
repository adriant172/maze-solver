from tkinter import Tk, BOTH, Canvas

class Window:
    """This is where we define the class that creates the game window"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("It all starts here!")
        self.canvas = Canvas(self.__root, bg="black", height=self.height, width=self.width)
        self.canvas.pack()
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """This is a method that keeps rendering the window"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """This will only close the window once the window 
        running toggle has been switched to false"""
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        """This toggles the window running boolean to off"""
        self.window_running = False

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    def draw(canvas, color):
        canvas.create_line(self.a.x, self.a.y,self.)

         