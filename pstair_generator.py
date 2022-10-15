################################################
# PENROSE-STAIRCASE-GENERATOR v1.0             #
# This program calculates ratios for           #
# the "Impossible-Staircase".                  #
# (c) 2022 by F. Lehr                          #
# https://www.ferdinandlehr.de                 #
# ferdinand@ferdinandlehr.de                   #
################################################

import csv

#Calculates the number of staircases for a given (always even) stairsum.
#def P(g):
#    return int((1/8)*g**2-(3/4)*g+1)

#Calculates the number of staircases for a given (always even) stairsum.
def P2(g):
    c=0
    p=1
    k=2
    i=6
    while(i<=g):
        #print("i,g,c",i,g,c)
        c=0
        for j in range(p):
            c+=1
        #print(c)
        p+=k
        k=k+1
        i+=2
    return c


#Set of all PStairs to an upper limit : nth Stairsum
def tz(n):
    r=0
    for i in range(1, n+1):
        r += P2(2*i+4)
    return int(r)

#Calculates the nth stairsum
def NG(n):
    return(n*2+4)

#Calculates the stairsum g for the nth Pstair
def SNP(n):
    k=1
    while(tz(k)<n):
        k=k+1
    return NG(k)

#calculates how many stairsums occur up to a given g (including stairsum for g)
def SBG(g):
    n=1
    while(NG(n)<g):
        n=n+1
    return n

#Calcs l of the nth PStair.
def LONP(n):
    g=SNP(n)
    #print("Stairsum =",g)
    rpos=P2(g)
    #print("Number of stairs with that stairsum p =", rpos)
    m=int((g-4)/2) #calculate how many times d=l for a given g
    #print("Position within that stairsum range rpos =", rpos)
    #print("m =", m)
    tpos = tz(SBG(g))#n+rpos-1
    #print("Cursor position total tpos = ", tpos)
    u=m
    for j in range(m+1):
        d=1 #divisor
        l=-1 #length
        for i in range(u):
            l=g/d
            d=d+1
            tpos-=1
            #print ("l =", l, "tpos=", tpos)
            if (tpos+1)==n:
                return l
        u=u-1
   
# returns 3,4,4,5,5,5,6,6,6,6,...
def AINC(p):
    n=1000000000
    c=0
    for i in range(1,n+1):
        for k in range(1,i+1):
            c+=1
            if(c==p):
                return i+2

     
#calcs a of the nth pstair
def A_of_NP(n):
    g=SNP(n)
    rpos=P2(g)
    tpos = tz(SBG(g)-1)+1
    #print("rpos,tpos,",rpos,tpos)
    return(AINC(n-tpos+1))

#calcs b of the nth pstair
def B_of_NP(n):
    a=A_of_NP(n)
    g=SNP(n)
    return int(((g+4)/2)-a)

# returns 2,2,3,2,3,4,2,3,4,5,2...
def CINC(p):
    n=100000000
    c=0
    for i in range(1,n+1):
        for k in range(1,i+1):
            #print(i,k)
            c+=1
            if(c==p):
                return k+1

#calcs c of the nth pstair
def C_of_NP(n):
    g=SNP(n)
    rpos=P2(g)
    tpos = tz(SBG(g)-1)+1
    #print("tpos=",tpos)
    return(CINC(n-tpos+1))

#calcs d of the nth pstair
def D_of_NP(n):
    a=A_of_NP(n)
    b=B_of_NP(n)
    c=C_of_NP(n)
    return a+b-c

#calculate and print the nth pstair
def PStair_nth(n):
    a=A_of_NP(n)
    b=B_of_NP(n)
    c=C_of_NP(n)
    d=a+b-c
    g=SNP(n)
    l=LONP(n)
    print(a,b,c,d,g,l)
    
#calculate and print 1st pstair to nth pstair
def PStairs_to_n(n):
    for i in range(1,n+1):
        PStair_nth(i)

#calculate and write 1st pstair to nth pstair to CSV-file
def PStairs_to_n_CSV(n):
    f = open('pstairs.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(f,delimiter=',')
    for i in range(1,n+1):
        a=A_of_NP(i)
        b=B_of_NP(i)
        c=C_of_NP(i)
        d=a+b-c
        g=SNP(i)
        l=LONP(i)
        #print(a,b,c,d,g,l)
        #data = [a,b,c,d,g,str(l).replace('.', ",")]
        data = [a,b,c,d,g,l]
        writer.writerow(data)
    f.close()

#Main-Program
print("PENROSE-STAIRCASE GENERATOR v1.0")
n=10
print("Calculating the first", n, "Penrose-Stairs")
print("a b c d sum len")
PStairs_to_n(n)
