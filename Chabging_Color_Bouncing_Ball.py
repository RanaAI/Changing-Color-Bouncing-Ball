"""
Creating a Bouncing Ball Application with Python
 Language. The Bouncing Ball Application has the 
 specialty that it can change the color of the 
 bouncing ball itself at every new run.
"""

# importing libraries

from graphics import Canvas
import random
import time

# initialization constants

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 450
BALL_DIAMETER = 25
INITIAL_VELOCITY = 5
START_X = 0
START_Y = 0
DELAY = 0.01

def main():
    # creating the canvas

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # control the color
    color = random_color()

    # other variable 
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    ball_x = START_X
    ball_y = START_Y
    
    # Creating the bouncing ball
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_DIAMETER,
                              ball_y + BALL_DIAMETER,
                              color)

    # Changing the dircetion of ball and function continuty                         
    while True:
        if (ball_x < 0) or (ball_x + BALL_DIAMETER >= CANVAS_WIDTH):
            x_velocity = -x_velocity
            
        if (ball_y < 0) or (ball_y + BALL_DIAMETER >= CANVAS_HEIGHT):
            y_velocity = -y_velocity
            
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        time.sleep(DELAY)

# D
def random_color():
    colors = [ 'blue','purple', 'salmon', 'lightblue', 'cyan', 'forestgreen' ]
    return random.choice(colors)

if __name__ == '__main__':
    main()