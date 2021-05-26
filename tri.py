#imports
import turtle
import time
import random
#scoreBoard
score = 0
high_score = 0
#screen
wn = turtle.Screen()
wn.title("Triangle Knigdom-by Astin")
wn.bgcolor('cyan')
wn.setup(width=1920, height=1080)
wn.tracer(0)
#head of snake
head = turtle.Turtle()
head.speed(0)
head.shape('triangle')
head.color('red')
head.penup()
head.goto(0,0)
head.direction = "stop"
#food
food = turtle.Turtle()
food.speed(0)
food.color('pink')
food.shape('triangle')
food.penup()
food.goto(0,100)
segments = []
#bomb
bomb = turtle.Turtle()
bomb.speed(0)
bomb.color('black')
bomb.shape('circle')
bomb.penup()
segments = []
#Ultra_bomb
bob = turtle.Turtle()
bob.speed(10)
bob.color('green')
bob.shape('circle')
bob.penup()
segments = []
#myself
twr = turtle.Turtle()
twr.speed(0)
twr.shape('square')
twr.color('red')
twr.penup()
twr.hideturtle()
twr.goto(0,300)
twr.write("***Created by TheWordRaptor***", align='center', font=('ds-digital', 32, 'normal'))
#score_board
sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('black')
sc.penup()
sc.hideturtle()
sc.goto(0,280)
sc.write("score = 0, High Score = 0", align='center', font=('ds-digital', 22, 'normal'))
#function
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
#keyboard
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')
#mainloop
while True:
    wn.update()
    #check collision with border area
    if head.xcor()>640 or head.xcor()<-650 or head.ycor()>270 or head.ycor()<-330:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()
        #reset score
        score = 0
        #reset delay
        delay = 0.1
        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
    #check collision with food
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-630,620)
        y = random.randint(-320,250)
        food.goto(x,y)
        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("triangle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 
    if high_score >=20:
        if head.distance(bomb) <20:
            # move the bomb to random place
            x = random.randint(-630,620)
            y = random.randint(-320,250)
            bomb.goto(x,y)
            #shorten the delay
            delay += 0.005
            #increase the score
            score -= 10
            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 
    if high_score >=50:
       if head.distance(bob) <20:
            # move the Ultra-bomb to random place
            x = random.randint(-630,620)
            y = random.randint(-320,250) 
            bob.goto(x,y)
            #shorten the delay
            delay += 0.01
            #increase the score
            score -= 50
            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 
    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            #update the score     
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(0.1)
wn.mainloop()
