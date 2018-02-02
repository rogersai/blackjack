# y = -9.8T^2 + VoT
# x = VoT
# dy = -19.6T + Vo
# dx = Vo
# dir = arctan((-19.6t + Vo)/Vo)
import turtle
import math
import random

# Declare variables
vel_x = 0.0 # The current X velocity of the turtle
vel_y = 0.0 # The current Y velocity of the turtle
turt_v = 0.0 # The current speed of the turtle's movement
turt_d = 0.0 # The current direction of the turtle's movement

TIME_INTERVAL = 0.1 # Sets the time interval between drawing updates.
                    # A smaller number gives a smoother animation
                    # This is intended to be measured in seconds

turtle.setup(500, 500) # This initializes the canvas the turtle will draw on
turtle.speed(2) # Sets the turtle's drawing speed, from 1 - 10

for i in range(0,3): # We're going to shoot 3 turtles
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-200, -200) # Puts the turtle back at the starting location
    
    INITIAL_HEADING = 90.0 * random.random() # Sets a randomized starting angle in degrees
    INITIAL_VELOCITY = 200.0 + 200.0 * random.random() # Sets a randomized starting speed in m/s

    # Sets the speed and direction and makes the turle's first move
    turt_v = INITIAL_VELOCITY * TIME_INTERVAL
    turt_d = INITIAL_HEADING
    turtle.setheading(turt_d)
    turtle.showturtle()
    turtle.pendown()
    turtle.forward(turt_v)

    # Figure out the starting x and y components of the turtle's movement, using Trig Functions!
    vel_x = math.cos(INITIAL_HEADING * math.pi / 180) * INITIAL_VELOCITY * TIME_INTERVAL
    vel_y = math.sin(INITIAL_HEADING * math.pi / 180) * INITIAL_VELOCITY * TIME_INTERVAL

    # Keep drawing until the turtle hits the ground
    while(turtle.ycor() > -200):
        vel_y -= 9.8 * TIME_INTERVAL # Apply the effects of gravity
        turt_v = math.sqrt(vel_x**2 + vel_y**2) # Recompute speed (You remember the Pythagorean Theorem, right?)
        turt_d = math.atan(vel_y/vel_x) * 180 / math.pi # Recompute direction
        turtle.setheading(turt_d)
        turtle.forward(turt_v) # Draw the next move

