num = input("enter a value: ")

def checkPal(num):
    temp = num
    rev = num[::-1]
    #print("rev is",rev)
    if  rev == num:
        return "pal"
    else :
        return "Not"
    

def createStr(num):
    if checkPal(num) == "pal":
        print(num)
    else:
        leng = len(num) # lengtgh of string
        for j in range (leng-1): # loop from 0 to length -1
            if num[j] != num[leng-j-1]: # check if starting character/num is not eual to the last character/num (in loop every time it will check for the next substring)
                newStr = num[:leng-j]+num[j] # add or insert first characters to the last or required position
                #print(newStr)
                createStr(newStr) # recurssion used to fetch the new string just created and check validity
                break # break when recurssion limit exceeds
            
createStr(num) # calling CreateStr function