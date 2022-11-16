'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import random

import arcade
import math
arcade.open_window(600,600,"Pycasso")
arcade.set_background_color((0,0,0))
arcade.start_render()

#Draw the background
for i in range(300):
    x = random.randrange(0,600)
    y = random.randrange(0,600)
    z = random.randrange(5,50)
    a = random.randrange(5,25)
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    arcade.draw_circle_outline(x,y,z,(r,g,b),a)
    for i in range(2):
        x = random.randrange(0, 600)
        y = random.randrange(0, 600)
        h = random.randrange(5, 50)
        w = random.randrange(5, 50)
        a = random.randrange(5, 25)
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        t = random.randrange(0,360)
        arcade.draw_rectangle_outline(x,y,w,h,(r,g,b),a,t)
# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                        start_angle, end_angle, 10)


arcade.finish_render()
arcade.run()