import turtle as t
t.colormode(255)
t.bgcolor('beige')
i=1
blue=255


while (blue>50):
    t.pensize(i)
    t.pencolor(150,100,blue)  #색 서서히 변화
    t.fd(i*10)
    t.lt(70)
    blue-=10  #blue=blue-10
    i+=1  #i=i+1
