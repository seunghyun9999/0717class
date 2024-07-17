def  구구단 (num):
    for i in range(1,10):
        num2 = num * i
        print(num,'X',i,'=',num2)


while True :
    b = int(input('숫자를 입력하시오.'))
    구구단(b)
