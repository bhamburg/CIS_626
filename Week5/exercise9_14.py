from tkinter import * # Import tkinter

width = 220
height = 100

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Arrow Keys") # Set a title

        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        self.x1 = (width / 2) - 5
        self.y1 = (height / 2) - 5
        self.canvas.create_oval(
            self.x1, self.y1, self.x1 + 10, self.y1 + 10
        
        # Bind canvas with key events
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()

        window.mainloop() # Create an event loop

    def up(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 5, tags = "line")
        self.y -= 5
        
    def down(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 5, tags = "line")
        self.y += 5
        
    def left(self, event):
        self.canvas.create_line(self.x, self.y, self.x - 5, self.y, tags = "line")
        self.x -= 5
    
    def right(self, event):
        self.canvas.create_line(self.x, self.y, self.x + 5, self.y, tags = "line")
        self.x += 5

MainGUI()
