def fun(a,*args,s='!'):
    print(a,s)
    for i in args:
        print(i,s)
fun(10,20)