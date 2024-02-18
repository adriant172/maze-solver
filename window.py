from tkinter import Tk, BOTH, Canvas

class Window:
    """This is where we define the class that creates the game window"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("It all starts here!")
        self.canvas = Canvas(self.__root, bg="white", height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
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
    
    def draw_line(self,line,color):
        line.draw(self.canvas, color)

class Point:
    """Simple class to create points based ona X and Y axis"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    """ This class creates a line between two points"""   
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def draw(self, canvas, color):
        canvas.create_line(
            self.a.x, self.a.y,self.b.x, self.b.y, fill=color, width=2
            )
        canvas.pack(fill=BOTH, expand=1)
