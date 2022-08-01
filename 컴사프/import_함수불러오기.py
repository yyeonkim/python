import random as r
import toDo as t

todo_list=[t.eat,t.donate,t.volunteer,t.clean,t.coding]  #함수도 list 가

ans='1'
while ans=='1':
    index=r.randint(0,len(todo_list)-1)  #그냥 (0,4)해도 동일
    todo_list[index]()
    ans=input('continue?(yes:1, no:0)\n')
