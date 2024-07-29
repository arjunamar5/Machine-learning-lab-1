def r(list,a):
    if(a < 3):
        return "not possible"
    else:
        for i in range(0,a):
            ele = int(input())
            list.append(ele)

        a = max(list)
        b = min(list)
        return a-b

a = int(input("enter the no of elements in the list :"))
list = []

print(r(list,a))
