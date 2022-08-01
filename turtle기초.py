import turtle as t

t.home() #(0,0)으로 돌아옴 #방향까지 제자리 #그리면서 올 수 있음

t.setheading(90) #해당 각도로 방향틀기
t.seth(90)

t.stamp() #숫자를 주면서 도장을 찍는다
t.clearstamp(숫자) #해당 도장 숫자를 입력하여 도장 지우기
t.clearstamps()  #모든 도장 지우기

t.undo()  #한 번 되돌리기

t.positon()  #거북이 좌표
t.pos()

t.xcor()  #좌표 알려줌
t.ycor()

t.heading() #현재 방향(각도) 알려줌

t.distance(x,y) #해당 좌표와의 거리 출력

t.degrees(360) #각도 한 바퀴 단위 설정

t.radins() #라디안으로 각도 설정

t.pen(fillcolor = 'black', pencolor = 'red', pensize = 10) #펜 설정
'''
“shown”: True/False

“pendown”: True/False

“pencolor”: color-string or color-tuple

“fillcolor”: color-string or color-tuple

“pensize”: positive number

“speed”: number in range 0..10

“resizemode”: “auto” or “user” or “noresize”

“stretchfactor”: (positive number, positive number)

“outline”: positive number

“tilt”: number
'''

t.isdown() #pendown되어 있으면 True, 아니면 False

t.color('색깔') #pencolor, fillcolor 모두 포함

t.filling() #채우기 중이면 True, 아니면 False
#활용
if t.filling():
    t.pensize(5)
else:
    t.pensize(3)

t.reset() #그림 모두 초기화

t.clear() #화면만 지움 #거북이는 가만히 있음

t.write(arg, move=False, align='left',font=('Arial',8,'normal')) #글쓰기
'''
arg – object to be written to the TurtleScreen

move – True/False

align – one of the strings “left”, “center” or right”

font – a triple (fontname, fontsize, fonttype)
'''

t.hideturtle()
t.ht()

t.showturtle()
t.st()

t.pendown()
t.pd()
t.penup()
t.pu()

t.isvisible() #거북이 보이면 True, 아니면 False

t.shape(name) #모양 바꾸기
'''
name = “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
'''

t.shapesize(stretch_wid, stretch_len, outline) #기본은 (1,1,1) #크기바꾸기
t.turtlesize()

t.tilt(angle) #거북이 방향은 바뀌지만 그리는 각도는 동일

t.settiltangle(angle) #현재 tiltangle과 상관없이 해당 각도로 방향 전환

t.tiltangle() #현재 tiltangle 반환

t.onclick()

t.onrelease()

t.ondrag()

t.begin_poly()
t.end_poly()
t.get_poly()

t2 = t.Turtle() #새로운 인스턴스 생성
t3 = t2.clone() #t2 자리에서 클론 t3 생성

pet = t.getturtle() #pet으로 객체 생성; Turtle object 그 자체
pet = t.getpen()

s = t.getscreen()  #TurtleScreen object 생성/ screen 관련 명령만 가능
s.bgcolor('blue') 등
