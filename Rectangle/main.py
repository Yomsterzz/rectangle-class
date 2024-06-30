import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Rectangle"

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

color = (r,g,b)
width = random.randint(50,200)
length = random.randint(50,200)

class Rectangle:
    def __init__(self, color, width, length, x, y):
        self.color = color
        self.width = width
        self.length = length
        self.x = x
        self.y = y
        self.xvel = 200
        self.yvel = 0

    
    def draw_rectangle(self):
        self.pos = (self.x, self.y)
        screen.draw.filled_rect(rRect(self.x, self.y, self.width, self.length), color=self.color)
        
    

rectangle1 = Rectangle(color, width, length, 400, 300)

def draw():
    rectangle1.draw_rectangle()

def update():
    pass

pgzrun.go()