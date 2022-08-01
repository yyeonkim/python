#9단만
for i in [1,2,3,4,5,6,7,8,9]:
    print('9*',i,'=',9*i)

#2단부터 9단
for dan in range(10):
    for i in [1,2,3,4,5,6,7,8,9]:
        print(dan, '*',i,'=',dan*i)

#0단없애기
for dan in range(1,10,1):
    for i in [1,2,3,4,5,6,7,8,9]:
        print(dan,'*',i,'=',dan*i)
