#List

L1=[]
L2=[1,2,3]
L3=['You','can','do','it']
L4=[1,2,'You','can']
L5=[1,2,['You','can']]

#인덱싱
L2[0] #1
L2[-3] #=L2[0]
L2[-1] #3

L5[2][0] #You

#슬라이싱
L3[2:]
L5[0:2] #1,2
L5[2][1:] #can

#더하기
L2+L3

#반복/곱하기
L5*2

#길이구하기
len(L5) #3

#수정/삭제
L3[0] = 'She'
del L5[0:2]

#값 추가하기
L1.append(4,5,6)

#정렬하기
L3.sort()

#뒤집기
L2.reverse()

#위치반환_index
L5.index(2) #1

#삽입하기_insert(특정위치)
L4.insert(2,3) #[2]자리에 3삽입

#요소제거_remove #같은 값이 여러 개일 경우 첫 번째부터 제거
L5.remove(['You','can'])

#요소 끄집어내기_pop
L3.pop()  #맨 마지막 요소를 끄집어내고 삭제
L4.pop(2) #'You'끄집어내고 삭제

#요소 개수세기_count
L5.count('You')  #0
L5,count(['You','can']) #1

#리스트 확장_extend
L1.extend('Good')  #['G','o','o','d']
L1.extend(['Good'])  #['Good'] #list를 입력하면 그 안의 값을 추가
