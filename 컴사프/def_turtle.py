import turtle as t
import random as r

def rect(a):  #사각형 그리기
    t.pencolor(a)
    for k in range(4):
        t.fd(10)
        t.rt(90)

def jump_fd(amount):  #점프하기
    t.penup()
    t.fd(amount)
    t.pendown()

def rect_line(c):  #c색깔로 사각형+앞으로15점프
    for i in range(5):
        rect(c)
        jump_fd(15)

#-------main---------

s=t.getscreen()
t.colormode(255)
t.speed('fastest')
w=int(s.canvwidth*2/3)
h=int(s.canvheight*2/3)

for j in range(5):
    s_color=(r.randint(30,200),r.randint(30,200),r.randint(30,200)) #랜덤색깔
    cx=r.randint(-w,w); cy=r.randint(-h,h)  #랜덤좌표
    for k in range(8):  #s_color로 rect_line하고 45도 돌기 8번
        t.penup()
        t.goto(cx,cy)
        t.pendown()
        rect_line(s_color)
        t.rt(45)
