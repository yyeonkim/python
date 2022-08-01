print('Hi, nice to meet you.')
name=input('what\'s your name?\n')
print(name,', choose one color below, please. (write only the number!!)')
c=input('''1.blue
2.grey
3.pink
4.greenyellow
5.others\n''')
cs={'1':'blue','2':'grey','3':'pink','4':'greenyellow','6':'gold','7':'orange','8':'purple','9':'deepskyblue'}

#함수정의1_사람그리기
def peo():
    import turtle as t
    t.pendown() #얼굴
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.rt(20)
    t.fd(30)
    t.rt(70)
    t.pendown() #몸
    t.begin_fill()
    for k in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(60)
        t.rt(90)
    t.end_fill()
    t.penup()
    t.rt(130)
    t.fd(55)
    t.rt(140)
    t.color('red') #입
    t.pendown()
    t.begin_fill()
    for d in range(3):
        t.fd(30)
        t.rt(120)
    t.end_fill()
    t.penup()
    

#함수정의2_배경그리기
def draw():
    import turtle as t
    t.speed('fastest')
    t.bgcolor(cs[c])
    t.color('white')
    t.penup()
    t.goto(-250,300)
    t.pendown()
    t.begin_fill() #말풍선
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(150)
        t.rt(90)
    t.end_fill()
    t.penup()
    t.goto(125,150)
    t.pendown()
    t.begin_fill()
    t.rt(120)
    t.fd(80)
    t.goto(187,150)
    t.goto(125,150)
    t.end_fill()
    t.penup()
    t.home()
    t.goto(0,-250)
    t.begin_fill() #원
    t.circle(150)
    t.end_fill()
    t.penup()
    t.goto(-50,-55)
    t.color(cs[c])
    peo() #함수1
    t.goto(50,-55)
    t.color('cadetblue')
    peo() #함수1
    #글씨쓰기
    t.color('black')
    t.goto(-200,180)
    t.write('''I'm living to communicate with many people.
Would you like to join me?
I will go to meet you who have different
circumstance and personality from me.''','center',font=('Bradley Hand ITC',15))
    t.ht()


#함수정의3_소개하기
def introduce():
    while True:
        a=input('Alright. Then, do you want to know me? (y/n)\n')
        if a=='n':
            print('Well.. so sad. Then Bye~')
            break
        elif a=='y':
            draw() #함수2
            break
        else:
            print('Say y or n, please.')
        
        

#----------------실행-------------------
while True:
    while int(c)<1 or int(c)>5:
        print('Only choose one of them..')
        c=input('''1.blue
2.grey
3.pink
4.greenyellow
5.others\n''')
    if 1<=int(c)<=4:
        introduce() #함수3
        break
    elif int(c)==5:
        print('Then, choose here.')
        c=input('''6.gold
7.orange
8.purple
9.deepskyblue
10.go back\n''')
    while int(c)<6 or int(c)>10:
        print('Only choose one of them..')
        c=input('''6.gold
7.orange
8.purple
9.deepskyblue
10.go back\n''')
    if 6<=int(c)<=9:
        introduce() #함수3
        break
    elif int(c)==10:
        c=input('''1.blue
2.grey
3.pink
4.greenyellow
5.others\n''')

#나와 다른 색깔의 성격과 환경을 가진 다양한 사람들과
#자유롭게 소통하는 세상을 살아가는 것.
