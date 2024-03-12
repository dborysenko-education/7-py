import turtle
from random import randint 

screen = turtle.Screen()
screen.bgcolor("black")


def draw_squares(number):
    starting_angle = 0 
    t = turtle.Turtle()
    t.width(5)
    colors = ["blue", "red", "yellow", "green", "gray", "brown", "purple"]
    prev_color = 0
    def randcolor(colors, prev_color): 
        curent_color = randint(0,len(colors)-1)
        if curent_color != prev_color: 
            prev_color = curent_color
        else: 
            curent_color = randint(0,len(colors)-1)
        return colors[curent_color]
    for squares in range(number):
        # Draw a square
        
        t.setheading(starting_angle)
        t.color(randcolor(colors, prev_color))
        for angle in range(4):
            t.forward(100)  # Move the turtle forward by 100 units
            t.right(90)     # Turn the turtle right by 90 degrees
                
        starting_angle += 360 / number
        print(starting_angle)

    # Move the turtle's cursor 150 pixels to the right
draw_squares(18)
# Keep the window open until it's closed manually
turtle.mainloop()