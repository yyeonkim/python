answer=''  #아무거나
answer=input('영국의 수도는 어디일까요?')
while answer != '런던': 
    if answer!='런던':
        print('오답입니다! 다시 해보세요.')
        answer=input('영국의 수도는 어디일까요?')
else:  #즉 answer='런던' 이면
    print('정답입니다.')


##----------------------------------------------두번째 방법 (결과동일)
answer=''  #아무거나
answer=input('영국의 수도는 어디일까요?')
while True: 
    if answer!='런던':
        print('오답입니다! 다시 해보세요.')
        answer=input('영국의 수도는 어디일까요?')
    else:  #즉 answer='런던' 이면
        print('정답입니다.')
        break
