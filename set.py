#Set(집합)

s1=set([1,2,3]) #={1,2,3}
s2=set('Hello') #s2={'H','l','e','o'}
s3={4,5,6}
s4=set(['Hello'])  #={'Hello'}

##중복을 허용하지 않는다_자료형의 중복을 제거하기 위한 필터 역할로 종종 사용한다
##순서가 없다


s5={1,2,3,4,5,6}
s6={4,5,6,7,8,9}

'''
#교집합
s5&s6
s5.intersection(s6)

#합집합
s5|s6
s5.union(s6)

#차집합
s5-s6
s6-s5

s5.difference(s6)
s6.difference(s5)

#값 1개 추가하기_add
s1.add(4)

#값 여러 개 추가하기
s3.update([1,2,3])

#특정값 제거하기_remove
s1.remove(3)
s2.remove('H')
'''

