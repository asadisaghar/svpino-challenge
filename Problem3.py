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

def fibo100_list():
    outlist=[]
    for n in range(0, 100):
        outlist.append(fibo(n))
    return outlist

outlist=fibo100_list()
print outlist
