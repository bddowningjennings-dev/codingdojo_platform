import turtle
# the distance we want the pointer to travel each time
DIST = 100
for y in range(0, 50):
    turtle.right(-20*y)
    turtle.forward(DIST)

# for y in range(0,150):
#     turtle.circle(y*80)
#     turtle.forward(DIST)