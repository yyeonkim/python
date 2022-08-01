#1
def myaverage(a, b):
    average = (a+b)/2
    return(average)

#2
def get_max_min(data_list):
    get_max = max(data_list)
    get_min = min(data_list)
    return(get_max, get_min)

get_max, get_min = get_max_min(data_list)

#3


#4
def bmi(kg,cm):
    num = kg/(cm*0.01)^2
    if num < 18.5:
        print('마른체형')
    elif 18.5 <= num < 25.0:
        print('표준')
    elif 25.0 <= num <30.0:
        print('비만')
    else:
        print('고도 비만')

#5
def bmi_loop():
    while True:
        kg = input('몸무게를 입력하세요.\n')
        cm = input('키를 입력하세요.\n')
        num = float(kg)/(float(cm)*0.01)^2
        print('BMI:',num)
        if num < 18.5:
            print('마른체형')
        elif 18.5 <= num < 25.0:
            print('표준')
        elif 25.0 <= num <30.0:
            print('비만')
        else:
            print('고도 비만')

#6
def get_triangle_area(width, height):
    print('삼각형 면적:',width*height/2)

#7
def add_start_to_end(start, end):
    return sum(range(start, end+1))

#8
def list_return(data_list):
    relist=[]
    for i in data_list:
        relist.append(i[:3])
    return relist
        

