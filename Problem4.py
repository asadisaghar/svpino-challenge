#Write a function that given a list of non negative integers, arranges them such that they form the largest possible number
#For example, given [50, 2, 1, 9], the largest formed number is 95021.

test_solution = True

def test_pair(str1, str2):
    if str1+str2>str2+str1:
        return False, str1, str2
    else:
        return True, str2, str1

def test_all(sstr):
    ctrllist = False
    for i in range(len(sstr)-1):
        ctrl, sstr[i], sstr[i+1] = test_pair(sstr[i], sstr[i+1])
        ctrllist = ctrllist or ctrl
    if ctrllist:
        return True
    else:
        return False

def form_the_largest(inlist):
    instr = []
    for el in inlist:
        instr.append(str(el))
    sstr = sorted(instr, reverse=True)
    print sstr
    alldone = True
    while alldone:
        alldone = test_all(sstr)
        print sstr
    else:
        outstr = ''
        for i in range(len(sstr)):
            outstr += sstr[i]
        print outstr
        return outstr

if test_solution:
    inlist = [5, 2, 1, 9, 50, 56]
    outint = form_the_largest(inlist)
    print outint == '95655021'

    inlist = [5, 50, 56]
    outint = form_the_largest(inlist)
    print outint == '56550'

    inlist = [420, 42, 423, 4]
    outint = form_the_largest(inlist)
    print outint == '442423420'
