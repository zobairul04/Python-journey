def avg (a,b,c):
    sum= a+b+c 
    av=sum/3
    return av


print(avg(2,3,4))

print(" ")

def show (n):
    if n==0 :
        return
    
    print(n)
    show(n-1)

show(5)    