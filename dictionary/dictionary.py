#dictionary

dic={'name':'kim','phone':'01045861245','birth':'0722'}
a={1:'apple',2:['fruits','vegetables']}
grade={'pey':10,'julliet':99}
keys=['a','b','c','d']
value = 'fromkeys'




#딕셔너리 쌍 추가,삭제
a[3]='banana'
del dic[2]

#key로 value얻기
grade['juliet'] #99

##list는 key로 쓸 수 없다
##key가 중복되면 나머지는 무시된다

#key 리스트 만들기_keys
dic.keys()

for k in dic.keys():
    print(k)

list(dic.keys())

#value 리스트 만들기_values
a.values()

#key,value 쌍 얻기_items
a.items()

#key: value 쌍 모두 지우기
a.clear()

#Key로 Value 얻기_get
grade.get('pey')
a.get(2)
a.get(3) #None
a.get(3,'bar') #'bar'

#딕셔너리 key 조사하기_in
1 in a #True
'name' in dic #True

#리스트/튜플로 딕셔너리 만들기_fromkeys
dict.fromkeys(keys)
dict.fromkeys(keys,value)
dict.fromkeys(a,grade) #a의 value를 grade로 대체

#키 꺼내고 제거하기_pop
a.pop(1)

#키,값 꺼내고 제거하기_popitem
a.popitem()

#특정 key의 value return or 새로 추가_setdefault
a.setdefault(3,'cherry')  #새로 추가되고 'cherry' 출력
grade.setdefault('pey')  #10 출력
grade.setdefault('pey',10)
