#1
print('*****')

#2
print('*****\n'*4)
'or'
for j in range(4):
    for i in range(5):
        print('*',end='')
    print('')

#3
'''
i = 1
for i in range(5):  #변수 i와 for 안의 i와 다름
    print('*'*i)
    i += 1
'''
for j in range(5):
    for i in range(j+1):
        print('*',end='')
    print('')

#4
'''
i = 5
for i in range(5):
    print('*'*i)
    i -= 1
'''
for j in range(5):
    for i in range(5-j):
        print('*',end='')
    print('')
    

#5
'''
a=4; b=1
for a,b in range(5):  #변수 2개 안됨
    print(' '*a+'*'*b)
    a -= 1; b += 1
'''
for j in range(5):
    for i in range(4-j):
        print(' ',end='')
    for i in range(j+1):
        print('*',end='')
    print('')
    
#6
'''
a = 0; b = 5
for a,b in range(5):
    print(' '*a + '*'*b)
    a += 1; b -= 1
'''
for j in range(5):
    for i in range(j):
        print(' ',end='')
    for i in range(5-j):
        print('*',end='')
    print('')
    
#7_탑 쌓기
for j in range(5):
    for i in range(4-j):
        print(' ',end='')
    for i in range((j+1)*2-1):
        print('*',end='')
    print('')

#8_거꾸로 탑
for j in range(5):
    for i in range(j):
        print(' ',end='')
    for i in range((5-j)*2-1):
        print('*',end='')
    print('')

#9
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 302, 303], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
for floor in apart:
    for house in floor:
        if house in arrears:
            continue
        else:
            print('Newspaper delivery:',house)

