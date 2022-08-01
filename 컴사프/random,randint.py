import turtle as t
import random as r

angles=[70,-60,50,-40,60,-30]
s=t.getscreen()
w=s.canvwidth; h=s.canvheight
A='y'

while A=='y':  #y대답하면 다시 실행하도록
    t.clearscreen()
    t.pensize(3)
    t.speed('fastest')
    for i in range(7):
        #꼬리 들고 랜덤 위치로
        t.penup()
        t.goto(r.randint(-w/2,w/2),r.randint(-h/2,h/2))
    
        #꼬리 내리고 색깔 정하기
        t.colormode(255)
        t.pendown()
        t.pencolor(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    
        #라인 그리기
        for k in range(6):
            t.circle(5)
            t.rt(angles[k])  #list[index]
            t.fd(40)
        t.circle(5)

    #사용자에게 묻기
    A=input('Continue? (y/n)\n')

    while A!='y' and A!='n':  #엉뚱한 대답**_사용자입장
        print('Tell me y or n.')
        A=input('Continue?')
        
    if A=='n':
        t.color('deep pink')
        style=('Arial',80,'bold') #tuple
        t.penup()
        t.home()
        t.pendown()
        #입력,폰트(글꼴,크기,상태),위치
        t.write('Good Bye!!!',font=style,align='center')
        t.hideturtle()
        
