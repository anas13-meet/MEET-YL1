def divisors():
    mynum=  raw_input ('choose a number:')
    mynum= int(mynum)
    i=1
    divgroup = []
    for i in xrange(1,mynum/2+1):
            if (mynum % i == 0):
                divgroup.append(i)
                print i 
            i=i+1
    print mynum
    divgroup.append(mynum)
    

