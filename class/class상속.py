#다른 클래스에 이미 구현된 메서드나 속성을 상속한 클래스에서는
#그러한 메서드나 속성을 그대로 사용할 수 있게됩니다.

#클래스의 상속을 또 다른 관점에서 생각해보면 클래스를 상속한다는 것은
#부모 클래스의 능력을 그대로 전달받는 것을 의미합니다.

class Parent:
    def can_sing(self):
        print('Sing a song')

father = Parnet()
fater.can_sing()

class LuckyChild(Parent): #상속받고자 하는 클래스 이름
    pass
child1 = LuchkyChild()
child1.can_sing()

class UnLuckyChild:
    pass
child2 = UnLuckyChild()
child2.can_sing() #노래 부를 수 없음

#어떤 클래스를 상속하면 부모 클래스의 모든 것을 내 것처럼 사용할 수 있고,
#자신의 클래스에 메서드를 더 구현한다면 ‘플러스알파’가 되는 것입니다.

class LuckyChild2(Parent):
    def can_dance(self):
        print('Shuffle Dance')
