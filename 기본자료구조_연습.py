#1
naver_closing_price = [474500, 461500, 501000, 500500, 488500]

#2
print(max(naver_closing_price))
'or'
max_price = max(naver_closing_price)
print(max_price)


#3
print(min(naver_closing_price))
'or'
min_price = min(naver_closing_price)
print(min_price)

#4
p = naver_closing_price
print(max(p)-min(p))
'or'
print('가격차:',max(p)-min(p))

#5
print('수요일 종가:',p[2])

#6
naver_closing_price2 ={'09/07':474500, '09/08':461500, '09/09':501000, '09/10':500500, '09/11':488500}

#7
print(naver_closing_price2['09/09'])
