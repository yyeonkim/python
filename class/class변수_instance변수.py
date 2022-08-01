class Account:
    num_accounts = 0
    def __init__(self, name): #initialize: 클래스 생성자(생성될 때 자동 호출)
        self.name = name #인스턴스 변수: 인스턴스 네임스페이스에 존재
        Account.num_accounts += 1 #클래스 변수: 클래스 네임스페이스에 존재
    def __del__(self):  #delete: 클래스 소멸자(소멸될 때 자동 호출)
        Account.num_accounts -= 1

kim = Account('kim') #계좌생성
lee = Account('lee')

kim.name #각 계좌에 대한 소유자 정보는 인스턴스 변수인 name이 바인딩
lee.name

kim.num_accounts #은행에서 개설된 총 계좌의 개수: 2
lee.num_accounts #인스턴스 네임스페이스에 없으므로 클래스에서 가져옴

Account.num_accounts
#여러 인스턴스가 서로 공유해야 하는 값은 클래스 변수를 통해 바인딩해야 합니다.
