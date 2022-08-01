import turtle as t
t.speed('fastest')

#육각형그리기
def hexa():
    for i in range(6):
        t.fd(10)
        t.rt(60)

#육각형라인 그리기
def hexa_line():
    for i in range(5):
        hexa()
        t.penup()
        t.fd(20)
        t.pendown()

#------main------
for i in range(8):
    hexa_line()
    t.penup()
    t.goto(0,0)
    t.rt(45)
    t.pendown()
