# Move a circle using keys
# Author: Brian Hamburg

from tkinter import * # Import tkinter

width = 200
height = 100

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Moving Circle") # Set a title
        
        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.x = (width / 2) - 10
        self.y = (height / 2) - 10
        self.canvas.pack()
        self.canvas.create_oval(
            self.x, self.y, self.x + 20, self.y + 20, tags = "oval")
        
        # Bind canvas with key events
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()
        
        window.mainloop() # Create an event loop
        
    def down(self, event):
        self.canvas.delete(ALL)
        self.canvas.create_oval(
            self.x, self.y + 10, self.x + 20, self.y + 30, tags = "oval")
        self.y += 10

    def up(self, event):
        self.canvas.delete(ALL)
        self.canvas.create_oval(
            self.x, self.y - 10, self.x + 20, self.y + 10, tags = "oval")
        self.y -= 10
        
    def left(self, event):
        self.canvas.delete(ALL)
        self.canvas.create_oval(
            self.x - 10, self.y, self.x + 10, self.y + 20, tags = "oval")
        self.x -= 10
    
    def right(self, event):
        self.canvas.delete(ALL)
        self.canvas.create_oval(
            self.x + 10, self.y, self.x + 30, self.y + 20, tags = "oval")
        self.x += 10

MainGUI()
