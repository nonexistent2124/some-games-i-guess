import turtle
import time

p = turtle.Turtle()
e = turtle.Turtle()
sct = turtle.Turtle()
sct.color("black")
sct.penup()
sct.hideturtle()
sct.goto(270, 350)

window = turtle.Screen()
screen_w = 800
screen_h = 800
window.setup(screen_w, screen_h)
caught = False
score = 0

def update_score():
    sct.clear()
    sct.write(f"Score: {score}", align="left", font=("Helvetica", 16, "normal"))

def fwd():
    p.fd(10)
    check_bound()
def back():
    p.bk(10)
    check_bound()
def turn_r():
    p.rt(10)
    check_bound()
def turn_l():
    p.lt(10)
    check_bound()

def check_bound():
    p_xcor = p.xcor()
    p_ycor = p.ycor()
    if p_xcor > screen_w / 2 or p_xcor < -screen_w / 2 or p_ycor > screen_h / 2 or p_ycor < -screen_h / 2:
        p.goto(0, 0)

p.color("blue")
p.shape("arrow")
e.color("red")
e.shape("arrow")
diff = 5 * window.numinput("Difficulty", "What shall the difficulty be? 1-10.")
if diff is None:
    exit(1)

pen_q = window.textinput("Show Paths?", "Show Paths? Yes or No.")
if pen_q == "Yes":
    p.pendown()
    e.pendown()
elif pen_q == "No":
    p.penup()
    e.penup()
else:
    exit(1)

e.goto(0, 200)

window.onkey(fwd, "w")
window.onkey(back, "s")
window.onkey(turn_r, "d")
window.onkey(turn_l, "a")

window.listen()

while not caught:
    e.setheading(e.towards(p))
    e.forward(diff)
    score += 0.2
    score = round(score, 1)
    update_score()
    time.sleep(0.2)
    if e.distance(p) < 8:
        caught = True
        p.hideturtle()
        e.hideturtle()
        sct.goto(-20,0)
        sct.clear()
        sct.write(f"You scored {score}!", font=("Helvetica", 16, "normal"))
        time.sleep(2)
        window.bye()
    else:
        pass


