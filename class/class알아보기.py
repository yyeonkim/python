#절차지향 프로그래밍:
'''데이터와 그 처리 함수가 분리돼 있고
함수를 순차적으로 호출함으로써 데이터를 조작하는 프로그래밍 방식'''
#함수만 정의해서 사용하면 변수 name, emial, addr를 계속 다르게 만들어줘야함

#객체지향프로그래밍:
'''데이터와 명함과 관련된 함수를 묶어서
명함이라는 새로운 객체(타입)를 만들고 이를 사용해 프로그래밍'''

#class: 변수와 함수를 묶어서 하나의 새로운 객체(타입)로 만드는 것
class BusinessCard:
    pass

#class 와 instance의 관계
card1=BusinessCard()       #인스턴스=클래스 (붕어빵과 붕어빵 틀)
                    #self를 쓰는 이유는 설정할 instance 이름을 알 수 없기에
class Business:      #첫 번째 값은 항상 자동으로 돌려준
    def set_info(self, name, email, addr): #class 내부에 정의된 함수: method
        self.name=name   #name 변수가 가리키던 값을 self.name에 바인딩
        self.email=email #'self.변수명' 형태의 변수를 '인스턴스 변수'라 한다.
        self.addr=addr
    def print_info(self):
        print('-'*15)
        print('Name:',self.name)
        print('Email:',self.email)
        print('Address:',self.addr)
        print('-'*15)

c1=Business()
c1.set_info('Yongyeon','kyy8403','Korea')
c1.print_info()
