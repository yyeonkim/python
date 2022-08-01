import turtle as t
import random as r
s=t.getscreen()
t.colormode(255)
t.speed('fastest')
w=int(s.canvwidth*2/3)  #문자
h=int(s.canvheight*2/3)

palette=['IndianRed','honeydew1','khaki','lavenderblush','LightSteelBlue','maroon4','MediumPurple1','OliveDrab']

#함수정의_정사각형
def rect():
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()

#함수정의_원(컵 손잡이)
def circle():
    t.pensize(4)
    t.circle(r.randint(10,30))


#-----------컵_그리기--------------
for j in range(len(palette)):  #palette 색만큼 반복
    t.penup()
    t.goto(r.randint(-w,w),r.randint(-h,h))  #랜덤 위치
    t.pendown()
    t.color(palette[j])
    for i in range(2):
        rect()
        t.rt(80)
        circle()
        t.rt(120)  #회전한 상태로 이동하니 컵이 그려질 때마다 각도가 다름
        
