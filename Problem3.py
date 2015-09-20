#Write a function that computes the list of the first 100 Fibonacci numbers.
#By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
#As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def fib():
    f0, f1 = 0, 1
    while True:
        yield f1
        f0, f1 = f1, f0+f1

def fibo_list(Nmax=10): #for Nmax<40 the excecution time is somewhat reasonable but not for larger Nmax. There must be a better algorithm!
    outlist=[]
    for n in range(Nmax):
        outlist.append(fibo(n))

    return outlist

def fibo_generator(Nmax=10):
    outlist = [0]
    tmp = fib()
    while len(outlist)<Nmax:
        outlist.append(tmp.next())
    return outlist

outlist=fibo_list()
print outlist
outlist2=fibo_generator()
print outlist2

print outlist==outlist2
