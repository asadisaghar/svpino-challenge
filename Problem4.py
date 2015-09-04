#Write a function that given a list of non negative integers, arranges them such that they form the largest possible number
#For example, given [50, 2, 1, 9], the largest formed number is 95021.
def form_the_largest(inlist):
    instr = []
    for el in inlist:
        instr.append(str(el))
    sstr = sorted(instr)
    outstr = ''
    for i in range(len(sstr)):
        outstr += sstr[len(sstr)-i-1]
    print outstr
    return outstr

inlist = [50, 2, 1, 9]
form_the_largest(inlist)
