def fibo(n):
    a=0
    b=1
    for i in range(0,n):
        print(a)
        a,b = b,b+a    

fibo(10)
