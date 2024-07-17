numbers = [100,200,300]
def VAT (a):
    result=[]
    for i in a:
        result.append(int(i*1.1))
    return result

print(VAT(numbers))