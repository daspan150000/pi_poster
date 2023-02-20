from graphics import *
from PIL import ImageGrab
import os
import convertapi
import calculate_pi as pical
import math


#todo:
#
#find a way to change the color dynamicaly with the current digit of pi.
#
#find a better way to calculate pi to the nth digit 
#
#find a better way to convert from eps to pdf
#or find a better way to save the image from the TK window.


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
    boxes = 20
    box_size = 10
    screen_width = 1920
    screen_height = 1070
    num = 2

    #154x83

    win = GraphWin("pi poster", screen_width, screen_height)
    win.setBackground("grey")
    
    digits = read_digits()
    for x in range(0, box_size * 65, box_size):
        for y in range(0, box_size * 154, box_size):
            position = (y, x)
            draw_rect(win, position, box_size, int(digits[num - 1]))
            print(num)
            num += 1
    
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