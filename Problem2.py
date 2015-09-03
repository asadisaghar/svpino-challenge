#Write a function that combines two lists by alternatingly taking elements.
#For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
def combine_lists(inlist1, inlist2):
    if len(inlist1)==len(inlist2):
        outlist = []
        for el in range(len(inlist1)):
            outlist.append(inlist1[el])
            outlist.append(inlist2[el])
        print outlist
        return outlist
    else:
        print "Enter lists of the same length"

def combine_lists_w_itertools(inlist1, inlist2):
    from itertools import izip
    outlist = []
    for (el1, el2) in izip(inlist1, inlist2):
        outlist.append(el1)
        outlist.append(el2)
    print outlist
    return outlist

inlist1 = ['a', 'b', 'c']
inlist2 = [1, 2, 3]
combine_lists(inlist1, inlist2)
combine_lists_w_itertools(inlist1, inlist2)

