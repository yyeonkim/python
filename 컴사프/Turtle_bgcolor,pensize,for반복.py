import turtle as t
t.colormode(255)
t.bgcolor(237,199,77)
t.pencolor('white')


#달팽이집 그리기
for i in range(1,16):
    t.pensize(i)
    t.fd(i*10)
    t.lt(90)
for k in range(10,201,20):
    t.fd(k+150)
    t.lt(60)
