import random as r
import cat_class as o #다른 py파일에서 실행할 때는 import 해야함

sam=o.Cat(14,'쌤이')  #object 생성; 같은 py파일일 경우 sam = Cat(14,'쌤이')
too=o.Cat(255,'뚜껑이')
garum=o.Cat(9,'가르마')
pol=o.Cat(0.8,'폴짝')

weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
my_cats=[sam,too,garum,pol]

for w in weekdays:
    print('\n'+w)
    '''
    for i in range(2):
        index=r.randint(0,len(my_cats)-1)
        my_cats[index].eat_food()
    for i in range(len(my_cats)):
        if (my_cats[i].hungry):
            print(my_cats[i].name,'배고파요ㅠㅠ')
    '''
    for i in range(len(my_cats)):
        print(my_cats[i].name,end=',')  #이름 끝에 ,를 붙임
        do=r.randint(0,len(my_cats)-1)
        if (do>=0 and do<3):my_cats[i].todo[do]()
        else:my_cats[i].todo[do](1)  #poop 함수의 argument 입력
