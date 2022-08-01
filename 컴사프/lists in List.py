import random as r
def lip(): print('lip')
def aa(): print('aa')

list=[lip,aa]

#lip or aa 랜덤 입
index=r.randint(0,1)
list[index]()
