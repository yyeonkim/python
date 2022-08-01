class Player:
    def __init__(self, index, power):
        self.id = 'Player'+index
        self.energy = 1000
        self.power = power
        self.do = [self.attack, self.heal, self.idle]
        self.status = ['energetic', 'so so', 'tired', 'dying', 'dead']
        self.energyLevel = [800, 500, 200, 50, 0]

    def attack(self, who):
        who.energy -= self.power*0.1

    def heal(self):
        self.energy += 100

    def idle(self):
        print(self.id,'do nothing..')

    def print_status(self):  #player의 상태 표시
        i=0
        while True:
            if self.energy >= self.energyLevel[i]:
                print(self.id,'is',self.status[i])
                break
            else:
                i+=1

    def get_status(self):
        i=0
        while True and i < len(self.status)-1: #오류: list index out of range
            if self.energy >= self.energyLevel[i]:
                break
            else:
                i+=1
        return self.status[i]

#player 생성
p1 = Player('1',3000)
p2 = Player('2',800)

#p2가 'dead'일 때까지 공격
i=0
while p2.get_status() != 'dead':
    p1.attack(p2)

