
def 학점 (a):
    result = 'error'
    if 80< a <=100 :
        result = 'A'
    elif 60< a <=80 :
        result = 'B'
    elif 40< a <=60 :
        result = 'C'
    elif 20< a <=40 :
        result = 'D'
    elif 0< a <=20 :
        result = 'E'
    else :
        print('잘못된 값입니다.')
    return result
num = int(input('학점을 입력하시오'))
result=학점(num)
print('학점은 ',result,'입니다.')