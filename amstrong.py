number = int(input("enter a number: "))
len_number= len(str(number))
temp = number
sum =0
while temp != 0:
    rem = temp%10
    temp = temp//10
    sum += pow(rem,len_number)
if number == sum:
    print("This is a amstrong number")
else:
    print("its not a amstrong number")