
def Amstrong_number(num):
    actual_num = num
    length = len(str(num))
    result = 0
    while num>0:
        res = num % 10
        result = result + res ** length
        num = num//10
    if actual_num == result :
        return "Amstrong number"
    else:
        return "not an amstrong number"
print(Amstrong_number(153))
print(Amstrong_number(424))





