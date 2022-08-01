import turtle as t
t.color('orange')
for a in range(3):
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()
    t.rt(120)
