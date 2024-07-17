def mes (x) :
    num = len(x)
    pay = 0
    if num <= 20 :
        pay = 50
        print('50 원 입니다.')
    else :
        pay = 100
        print('100원 입니다.')
    return pay
x = input('메세지 입력 하시오')
pay = mes(x)
print(pay)