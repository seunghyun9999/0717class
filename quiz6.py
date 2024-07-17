
def 홀짝 (x) :
    result = '몰라'
    if x%2 == 0 :
        result = '짝수'
    elif x%2 == 1 :
        result = '홀수'
    else :
        result = '이상한 값'
    return result

result = 홀짝(int(input('숫자를 입력하세요')))
print(result)