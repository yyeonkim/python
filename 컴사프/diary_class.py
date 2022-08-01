class Diary:

    def __init__(self,name,feel):
        self.name_feel=name+', feeling:'+feel  #변수설정
        self.hungry=3
        self.todo=[self.clean,self.draw,self.cook,self.eat] #리스트설정
        

    def clean(self):
        print('I cleaned my room.')

    def draw(self,paint):
        print('I drew',paint+'.')

    def cook(self,meal):
        print('I cooked',meal+'.')

    def eat(self,num):
        print('I ate.')
        if self.hungry-num==0:
            print('I\'m full.')
        else: print('I\'ll eat',self.hungry-num,'times more.')

    
