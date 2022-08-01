def eat():
    print('eat')

def donate():
    print('donate')

def volunteer():
    print('volunteer')

def clean():
    print('clean')

def coding():
    print('coding')


#자체test---------------------

import random as r
List=[eat,donate,volunteer,clean,coding]
ans=3
'num=r.randint(0,len(List))'  #num이 하나로 정해져버려서 계속 같은 결과 나옴
while ans==3:
    num=r.randint(0,len(List)) 
    List[num]()
    Q=input('Conitnue? (y/n)')
    if Q=='y':
        continue
    else:
        print('End')
        break
    
