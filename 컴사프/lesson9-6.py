import turtle as t
s=t.getscreen()
for i in range(6):
    for a in range(4):
        t.fd(50)
        t.rt(90)
    for b in range(3):
        t.fd(25)
        t.rt(45)
        t.fd(25)
        t.lt(45)
    for c in range(6):
        t.fd(10)
        t.lt(60)
    t.penup()
    t.goto(0,0)
    t.rt(60)
    t.pendown()
