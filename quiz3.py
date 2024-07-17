def mes (x) :
    result = 0
    if len(x) <= 20 :
        result = 50
    elif len(x) > 20 :
        result = 100
    return result
입력 = input('메세지 입력 하시오')
결과 = mes(입력)
print(결과,'원')