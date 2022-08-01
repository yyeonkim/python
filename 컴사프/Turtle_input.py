import turtle as t
t.colormode(255)
t.bgcolor(114,214,191)
t.pencolor('orange')
limit=input('How many time do you want to draw?\n')

for i in range(0,int(limit)):
    t.fd(i*50)
    t.lt(80)
