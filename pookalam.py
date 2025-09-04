import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Setup turtle
t = turtle.Turtle()
t.speed(0)

# Draw maroon polygon
t.color("maroon")
t.penup()
t.goto(10, -50)   # adjust to center
t.pendown()

t.begin_fill()
for i in range(100):   # spikes around
    t.forward(300)
    t.left(100)
t.end_fill()

# Draw dark orange circle inside
t.penup()
t.goto(10,52)   # position for circle center
t.pendown()

t.color("orangered")
t.begin_fill()
t.circle(150)     # radius of circle (adjust as needed)
t.end_fill()


# Draw smaller maroon polygon inside the orange circle
t.penup()
t.goto(48, 169)    # move near circle center
t.pendown()

t.color("darkorange")
t.begin_fill()
for i in range(100):
    t.forward(222)   # smaller so it stays inside circle
    t.left(100)
t.end_fill()

# Draw orange circle inside
t.penup()
t.goto(119,190)   # position for circle center
t.pendown()

t.color("orange")
t.begin_fill()
t.circle(121)     # radius of circle (adjust as needed)
t.end_fill()

# Draw smaller yellow polygon inside the orange circle
t.penup()
t.goto(220, 178)    # move near circle center
t.pendown()

t.color("purple")   
t.begin_fill()
for i in range(100):
    t.forward(178)   # smaller so it stays inside circle
    t.left(100)
t.end_fill()

# Draw hexagon petals outline in the center
t.penup()
t.goto(162,75)      # go to center
t.pendown()
t.color("black")  # outline color
t.pensize(2)

for _ in range(6):   # 6 petals
    for i in range(6):   # draw hexagon
        t.forward(49)
        t.left(60)
    t.left(60)   # rotate for next petal

# Draw orange circle inside
t.penup()
t.goto(203,100)   # position for circle center
t.pendown()

t.color("white")
t.begin_fill()
t.circle(48)     # radius of circle (adjust as needed)
t.end_fill()

# Draw orange circle inside
t.penup()
t.goto(195,95)   # position for circle center
t.pendown()

t.color("darkgreen")
t.begin_fill()
t.circle(38)     # radius of circle (adjust as needed)
t.end_fill()

# Draw orange circle inside
t.penup()
t.goto(186,90)   # position for circle center
t.pendown()

t.color("orangered")
t.begin_fill()
t.circle(28)     # radius of circle (adjust as needed)
t.end_fill()

# Draw orange circle inside
t.penup()
t.goto(178,86)   # position for circle center
t.pendown()

t.color("yellow")
t.begin_fill()
t.circle(18)     # radius of circle (adjust as needed)
t.end_fill()


# Draw orange circle inside
t.penup()
t.goto(172,82)   # position for circle center
t.pendown()

t.color("red")
t.begin_fill()
t.circle(10)     # radius of circle (adjust as needed)
t.end_fill()

