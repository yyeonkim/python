#메서드의 인자(argument)로 어떤 문자를 기준으로 문자열을 나눌지 알려줘야 합니다. 'naver'와 'daum' 이라는 문자열 사이에는
#공백(blank)이 있으므로 공백을 기준으로 문자열을 나누면 됩니다.
#이를 위해 split(' ')과 같이 작은따옴표 사이에 공백을 하나 넣었습니다.

my_jusik = 'naver daum'
my_jusik.split(' ')
