def power(num,poww):
    if  poww == 0:
        return 1
    else :
        return num*power(num,poww-1)     


num=5
poww=5

print(power(num,poww))