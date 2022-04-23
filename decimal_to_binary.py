def decimalToBinary(n):
    return "{0:b}".format(int(n))
   
# Driver code
if __name__ == '__main__':
    
    myinput = input("enter a number:")
    convert_into_binary = int(decimalToBinary(myinput))
    print("binary of my input = ",convert_into_binary)
    my_list = list(map(int, str(convert_into_binary)))
    len_of_mylist = len(my_list)
    print("binary of the input = ",my_list)
    res = my_list.count(1)
    print("total 1 in binary = ",res)
    #print(len_of_mylist)
    print("index number of 1 in binary --------")
    for i in range(len_of_mylist):
        if(my_list[i]==1):
            result=i+1
            print(result)
    
            
