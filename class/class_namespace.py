class Stock:
    market='kospi'  

#네임스페이스: 변수와 바인딩된 객체 사이의 관계를 저장하고 있는 공간
dir() #dir 내장 함수; Stock 추가됨

Stock.market

s1=Stock()
s2=Stock()
dir()  #s1, s2도 각각 추가

#클래스 또는 인스턴스에 대한 네임스페이스를 확인하려면 __dict__ 속성을 확인
s1.__dict__
s2.__dict__ #둘 다 비어있음

#비어있는 인스턴스에 변수 생성하기
s1.market='kosdaq'
s1.__dict__

s2.market #인스턴스의 네임스페이스에 해당 이름이 없으면 클래스 네임스페이스로 이
s2.volume #클래스에도 없으므로 오류
