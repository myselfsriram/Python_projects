from cgi import print_form


a=int(input("Enter the number:"))
n1=0
n2=1
for i in range(0,a):
    print(n1)
    n=n1+n2
    n1=n2
    n2=n