Q='What is your best movie?\n'
menu ='''1.어바웃 타임
2.기생충
3.반지의 제왕
4.배트맨
5.레지던트 이블
6.기타'''
print('-'*20)
print(menu)
print('-'*20)

A=input(Q)

while(A<'1' or A>'6'):  #문자인 숫자로도 비교가능  #사용자경험 고려
    print('enter the number.')
    A=input(Q)

if A=='1':print('Romance? Mm.. I see..')
elif A=='2':print('I slept watching it.')
elif A=='3':print('Mm..fantasy is the best.')
elif A=='4':print('Mm.. it\'s a little dark.')
elif A=='5':print('I like it, too!')
else:
    A=input('Then what do you like?\n')
    print('Oh, '+A+' is your best. Interesting.')
