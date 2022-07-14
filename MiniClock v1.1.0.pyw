import turtle
import time
from random import randint

screen = turtle.Screen()
screen.title('时钟')
screen.setup(width=425, height=425, startx=-1, starty=0)
miao = turtle.Turtle()
fen = turtle.Turtle()
shi = turtle.Turtle()
date = turtle.Turtle()
miao.speed(0)
shi.speed(0)
fen.speed(0)
date.speed(0)
turtle.speed(0)
turtle.pensize(10)
turtle.hideturtle()
miao.hideturtle()
fen.hideturtle()
shi.hideturtle()
date.hideturtle()
s = m = h = 0
bg = turtle.Turtle()
screen.addshape('bg.gif')
screen.addshape('bg2.gif')
mybg = ['bg.gif', 'bg2.gif']
bgnum = randint(0, 1)
bg.shape(mybg[bgnum])
date.penup()
date.goto(-105, -100)
miao.pencolor('black')
fen.pencolor('blue')
shi.pencolor('orange')
# date.pendown()  write方法可以不用落笔


def change_bg():
    global bgnum
    if bgnum == 0:
        bgnum = 1
    else:
        bgnum = 0
    bg.shape(mybg[bgnum])


def miaozhen(s):
    screen.tracer()
    miao.clear()
    miao.pendown()
    miao.goto(0, 0)
    miao.pensize(2)
    miao.seth(s * 6 * (-1) + 90)
    miao.forward(150)
    miao.penup()
    miao.goto(0, 0)


def fenzhen(m):
    fen.pendown()
    fen.goto(0, 0)
    fen.pensize(3)
    fen.seth(90)
    fen.clear()
    fen.rt(m * 6)
    fen.forward(120)
    fen.penup()
    fen.goto(0, 0)


def shizhen(h, m):
    screen.tracer(30)
    shi.pendown()
    shi.goto(0, 0)
    shi.pensize(5)
    shi.seth(90)
    shi.clear()
    shi.seth((h * 30 + 0.5 * m) * -1 + 90)
    shi.forward(80)
    shi.penup()
    shi.goto(0, 0)


def write_date(y, mon, d, w):
    global y0, mon0, d0
    if y == y0 and mon == mon0 and d == d0:
        pass
    else:
        date.goto(-50, -60)
        date.write(w, font=('华文琥珀', 27, 'normal'))
        date.goto(-105, -100)
        date.write('%d年%d月%d日' % (y, mon, d), font=('隶书', 27, 'normal'))


screen.onkey(change_bg, "space")
screen.listen()

# 绘制钟表
screen.tracer(10)
turtle.dot(10)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)
turtle.penup()
turtle.home()
for i in range(12):
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.goto(0, 0)
    turtle.penup()
    turtle.forward(163)
    turtle.pendown()
    turtle.forward(32)
    turtle.pensize(2)
    turtle.pencolor('black')
    for j in range(4):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.rt(6)
        turtle.penup()
        turtle.forward(180)
        turtle.pendown()
        turtle.forward(20)

    turtle.penup()
    turtle.rt(6)

miaozhen(0)
shizhen(0, 0)
s = int(time.strftime('%S', time.localtime(time.time())))
m = int(time.strftime('%M', time.localtime(time.time())))
h = int(time.strftime('%I', time.localtime(time.time())))
miaozhen(s)
fenzhen(m)
shizhen(h, m)

y0 = int(time.strftime('%Y', time.localtime(time.time())))
mon0 = int(time.strftime('%m', time.localtime(time.time())))
d0 = int(time.strftime('%d', time.localtime(time.time())))
w0 = time.strftime('%A', time.localtime(time.time()))
date.goto(-50, -60)
date.write(w0, font=('华文琥珀', 27, 'normal'))
date.goto(-105, -100)
date.write('%d年%d月%d日' % (y0, mon0, d0), font=('华文琥珀', 27, 'normal'))

while True:
    s = int(time.strftime('%S', time.localtime(time.time())))
    m = int(time.strftime('%M', time.localtime(time.time())))
    h = int(time.strftime('%I', time.localtime(time.time())))
    y = int(time.strftime('%Y', time.localtime(time.time())))
    mon = int(time.strftime('%m', time.localtime(time.time())))
    d = int(time.strftime('%d', time.localtime(time.time())))
    w = time.strftime('%A', time.localtime(time.time()))
    turtle.delay()
    write_date(y, mon, d, w)
    miaozhen(s)
    fenzhen(m)
    shizhen(h, m)

# turtle.done()
