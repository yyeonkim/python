interest_stocks = {'Naver':10, 'Samsung':5, 'SK Hynix':30}


#items() 이용하기
for company, stock_num in interest_stocks.items():
    print('%s: Buy %s' % (company, stock_num))

#keys() 이용하기
for company in interest_stocks.keys():
    print('%s: Buy %s' % (company, interest_stocks[company]))
