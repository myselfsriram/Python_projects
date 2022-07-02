def count(a):
    temp=a
    temp=temp[::-1]
    for i in range(0,len(temp)):
        loc=temp[i]
        if(loc!=' '):
            print("%s =" %loc ,end= ' ')
            print("%02d " %cal(loc,a))
        temp=temp.replace(loc,' ')
def cal(a,b):
    count=0
    for i in a:
        for j in b:
            if(i==j):
                count+=1
    return count
a=input("Enter String:")
count(a)