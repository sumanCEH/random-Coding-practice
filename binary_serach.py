def binary_sort(my_list):
    for i in range(len(my_list)-1):
        for  j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j] # swapping 
        search_element = int(input("enter yoyr search element: "))        
        l=0
        h= len(my_list)-1
        m=0
        while h <= l:
            m = (h+l)//2
            if  my_list[m] < search_element:
                l =  m+1
            elif my_list[m] > search_element:
                r = m-1
            else:
                return m
        return -1                     


my_list = [12,56,8,44,20,27,38,52]

#calling
result = binary_sort(my_list)
if result == -1:
    print("found",my_list)
else :
    print("not found")    
