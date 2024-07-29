list=[2, 7, 4, 1, 3, 6]
def fun1(list):
    count=0                                  
    for i in list:
        for j in list:
            if((i+j)==10):
                print(i,j)
                count=count+1
    return count
print(fun1(list))
