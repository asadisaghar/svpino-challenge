# '''
# f(inlist) = 100
# if '+':
#     inlist[0] + f(inlist.remove(inlist[0])) = 100
# elif '-':
#     inlist[0] - f(inlist.remove(inlist[0])) = 100
# elif'':
#     instr = [str(el) for el in inlist]
#     inlist.remove(inlist[0])
#     inlist.remove(inlist[2])
#     f(instr[0]+inst[1], inlist) = 100
# '''
def funcplus(inlist, rhs, val):
    while len(inlist):
        print 'inlist0',inlist[0]
        val += inlist[0]
        inlist.remove(inlist[0])
        print 'val',val
        funcplus(inlist, rhs, val)
        return inlist

def funcminus(inlist, rhs, val):
    while len(inlist):
        print 'inlist0',inlist[0]
        val -= inlist[0]
        inlist.remove(inlist[0])
        print 'val',val
        funcminus(inlist, rhs, val)
        return inlist

def funcappend(inlist, rhs, val):
    while len(inlist):
        print 'inlist0',inlist[0]
        instr = [str(el) for el in inlist]
        val = str(val)
        if len(inlist)>1:
            val += instr[0]+instr[1]
            inlist.remove(inlist[0])
            inlist.remove(inlist[0])
            print 'val',val
        else:
            val += instr[0]
            inlist.remove(inlist[0])
            print 'val',val
        funcappend(inlist, rhs, val)
        return inlist


outlistp = funcplus(inlist=[1,2,3,4,5], rhs=10, val=0)
outlistm = funcminus(inlist=[1,2,3,4,5], rhs=10, val=0)
outlista = funcappend(inlist=[1,2,3,4,5], rhs=10, val='')
#print outstr
