#Tuple  #List와 가장 큰 차이점은 값을 수정하거나 삭제할 수 없다는 것!(그 외 동일)

t1=(1,2,3)
t2=3,'a','you'  #()생략 가능
t3=('a','b',1,(3,6,2))
t4=(2,)  #요소가 하나일 때는 ,꼭 붙이기

##값 접근하기
t1[0]  #1
t1[1]  #2

##슬라이싱; 지정한 자리부터 마지막까지
t3[2:] #(1,(3,6,2))

##더하기
t4 + t3  #요소가 합쳐진다
t2 + t3  #같은 요소가 있을 때는?

##곱하기
t4*2  #여러개 담긴다
t2[2]*3  #3번 print된다

#List처럼 len()가능
len(t1)
len(t3)  #4
