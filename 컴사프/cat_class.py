class Cat:
    def __init__(self, age,name):
        self.name = name
        self.age = age
        self.남은변 = 3
        self.hungry = True
        self.todo = [self.hello,self.grooming,self.eat_food,self.poop]

    def hello(self):
        print('냐옹~')

    def grooming(self):
        print('그루밍한다')

    def eat_food(self):
        print('사료먹기')
        self.hungry=False
        
    def poop(self,횟수):
        print('응아한다')
        self.남은변=max(self.남은변-횟수,0)
