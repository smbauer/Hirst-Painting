import colorgram
import turtle as t
import random


def init_turtle(start_pos=(-250, -250)):
    """set up turtle and screen starting conditions"""
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(start_pos)
    turtle.speed('fastest')

    return turtle


def get_colors(image, num_colors=20):
    """extract the rgb color scheme from an image"""
    color_scheme = colorgram.extract(image, num_colors)
    colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in color_scheme]

    return colors


def create_painting(turtle, colors, rows=10, cols=10):
    """create a rows x cols sized painting of randomly colored dots"""
    start_x = turtle.xcor()
    start_y = turtle.ycor()

    for i in range(rows):
        line_pos = start_y + (i * 50)
        turtle.setpos(start_x, line_pos)

        for j in range(cols):
            # draw a dot
            turtle.dot(20, random.choice(colors))
            # move forward 50 paces
            turtle.forward(50)


if __name__ == '__main__':
    tim = init_turtle()

    # init screen
    screen = t.Screen()
    screen.colormode(255)

    color_list = get_colors('hirst.jpg')
    # get rid of the background colors
    color_list = color_list[3:]

    create_painting(turtle=tim, colors=color_list)

    screen.exitonclick()
