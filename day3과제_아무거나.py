import turtle
t=turtle.Turtle()
t.shape('turtle')
t.shapesize(2,2)

while True:
    c=int(input('숫자를 입력하시오:'))
    if c%2==0:
        t.circle(50)
        t.fd(100)
    if c%2 != 0:
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.fd(100)
