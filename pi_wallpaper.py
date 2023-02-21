from graphics import *
from PIL import ImageGrab
import os
import convertapi
import calculate_pi as pical
import math


#secret
#IPcJQgBSsoHfyojo


def draw_rect(win, pos, size, color):
    colors = ("black" , "white", "red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "")
    color_value = colors[color]
    x = pos[0]
    y = pos[1]
    point1 = Point(x, y)
    point2 = Point(x + size, y + size)
    rect = Rectangle(point1, point2)
    txt = Text(Point(x + size / 2, y + size / 2), color)
    outline = 0
    if color == 0:
        txt.setTextColor("white")
    else:
        txt.setTextColor("black")
    rect.setOutline(color_value)
    rect.setFill(color_value)
    rect.setWidth(outline)
    rect.draw(win)
    size = int(size) / 2
    txt.setSize(int(size))
    txt.draw(win)
    
def read_digits():
    with open("pi_digits.txt") as txt:
        pi = txt.readlines()
    return pi

def main():
    box_size = 10
    screen_width = 1920
    screen_height = 1080
    num = 2

    digits = read_digits()

    win = GraphWin("pi poster", screen_width, screen_height)
    win.setBackground("grey")
    
    for y in range(0, math.floor(box_size * (screen_height / box_size)), box_size):
        for x in range(0, math.floor(box_size * (screen_width / box_size)), box_size):
            position = (x, y)
            draw_rect(win, position, box_size, int(digits[num - 1]))
            num += 1
    print(num - 1)
    # saves the current TKinter object in postscript format
    win.postscript(file="image.eps", colormode='color')

    convertapi.api_secret = 'IPcJQgBSsoHfyojo'
    convertapi.convert('pdf', {
        'File': 'image.eps'
    }, from_format = 'eps').save_files('image.pdf')

    os.remove("image.eps")

    win.getMouse()
    win.close()

    


#read_digits()
main()
#print(round(math.pi, 100))