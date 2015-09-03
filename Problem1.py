#Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
def sum_list_for(inlist):
    sumvalue = 0.
    for element in inlist:
        sumvalue += element
    print sumvalue
    return sumvalue

def sum_list_while(inlist):
    i = 0
    sumvalue = 0.
    while i<len(inlist):
        sumvalue += inlist[i]
        i += 1
    print sumvalue
    return sumvalue

def sum_list_recur(inlist):
    if len(inlist)==1:
        return inlist[0]
    else:
        return inlist[0]+sum_list_recur(inlist[1:])


inlist = [5, 10, 20, 2, 3]
forsum = sum_list_for(inlist)
whilesum = sum_list_while(inlist)
recursum = sum_list_recur(inlist)
print recursum
