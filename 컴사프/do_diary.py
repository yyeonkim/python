import diary_class as d  #import turtle as t
import random as r

weekend = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
feels = ['happy','sad','angry','soso']
paint = ['dog','cat','duck','my family']
meal = ['pasta','pizza','rice','icecream']

#t.Turtle()과 동일 (object생성)
yong = d.Diary('Yong-yeon',feels[r.randint(0,len(feels)-1)]) 
ji = d.Diary('Jimin',feels[r.randint(0,len(feels)-1)])
min = d.Diary('Minji',feels[r.randint(0,len(feels)-1)])
hyeo = d.Diary('Hyeon-seo',feels[r.randint(0,len(feels)-1)])

members = [yong,ji,min,hyeo]
#todo=[clean,draw,cook,eat] Diary class에 정의된 함수지만 여기선 실행 X


#--------main--------------

for w in weekend: #w는 숫자가아닌 요소
    
    m = r.randint(0,len(members)-1)
    do = r.randint(0,3)
    num = r.randint(1,3)
    c = r.randint(0,len(meal)-1)
    d = r.randint(0,len(paint)-1)

    
    print('\n'+w)
    print(members[m].name_feel)
    if do == 0:
        members[m].todo[do]()  #todo는 앞에는 self 붙여주기
    elif do == 1:
        members[m].todo[do](paint[d])
    elif do == 2:
        members[m].todo[do](meal[c])
    else:
        members[m].todo[do](num)
    


##아쉬운 점: 한 번 정해진 멤버의 기분이 계속 동일함 ㅠㅠ
##for 안에 d.Diary를 넣었을 때 에러가 남;
##'int' object has no attribute 'Diary'
