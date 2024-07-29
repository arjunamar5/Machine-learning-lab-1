def fun2(a,n):
    if(n==3):
        return "Range determination not possible"
    for i in range(n):
        ele=float(input())
        a.append(ele)
    max=a[0]
    for i in range(n):
        if(max<a[i]):
            max=a[i]
    min=a[0]
    for i in range(n):
       if(min>a[i]):
            min=a[i]
    return max-min
a=[]
n=int(input("Enter the number of elements in array"))
print(fun2(a,n))
