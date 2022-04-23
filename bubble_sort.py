def bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for  j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j] # swapping 
               

my_list = [12,56,8,44,20,27,38,52]
#calling
bubble_sort(my_list)
print(my_list)
