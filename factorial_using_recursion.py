def power(num):
    if  num == 0:
        return 1
    else :
        return num*power(num-1)     


num=5


print(power(num))