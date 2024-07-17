import random

result=[]
while int(len(result))<6:
    new = random.randint(1,45)
    if new in result :
        print(new,'번이 중복되어서 한번 더 실행')
    else :
        result.append(new)
print(result)