def linear_search(my_list,search_number):
    for i in range(len(my_list)-1):
        if my_list[i] == search_number:
            return i

    return -1
my_list = [12,56,8,44,20,27,38,52]
serach_number = int(input("enter  the input: "))

result = linear_search( my_list, serach_number)
if  result != -1:
    print("found postion no:",result+1)
else:
    print("not found")