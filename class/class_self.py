#'class알아보기'에서 생성한 객체는 빵만 먼저 구운후 나중에 팥소를 넣는 것과 같다.
class Myclass:  #클래스 인스턴스 생성과 초깃값 입력을 한 번에 처리하는 
    def __init__(self):  #생성자 (__가 들어간 것은 특별한 메서드이다.)
        print('객체가 생성되었습니다.')


class Foo:
    def function1():#self가 없으면 함수 실행 중 오류발생
        print('function1')

    def function2(self):
        print(id(self))
        print('function2')

#클래스 내에 정의된 self는 클래스 인스턴스임을 알 수 있다.***
f1=Foo()
print(id(f1))
f1.function2()

f2=Foo()
print(id(f2))
f2.function2()


#function1 부르기
Foo.function1() #클래스명.메서드(); 따로 클래스인스턴스가 안 만들었으므로..
#Foo.function2() #오류: func2()를 호출할 때 인자를 하나 빠트렸음
f3=Foo()
print(id(f3))
Foo.function2(f3) #인자를 넣어주자
#'인스턴스.메서드()'와 '클래스.메서드(인스턴스)'는 별 차이X
f3.function2()
