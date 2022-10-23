#-----------------------------------------------------------------#
# The Penrose-Staircase-Module v1.0 for PYTHON                    #
# (c) 2022 F. Lehr                                                #
# https://www.ferdinandlehr.de                                    #
# https://github.com/fl3000/Penrose-Staircase-Generator           #
#                                                                 #
# usage of this module:                                           #
#                                                                 #
#        import pstairs.py                                        #
#        p = PenroseStaircase(n) # n: n-th Penrose-Staircase      #
#        A = p.a                                                  #
#        B = p.b                                                  #
#        C = p.c                                                  #
#        D = p.d                                                  #
#        L = p.l                                                  #
#-----------------------------------------------------------------#

class PenroseStaircase:
    #Calculates the number of staircases for a given (always even) stairsum.
    def P2(self, g):
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
    def tz(self, n):
        r=0
        for i in range(1, n+1):
            r += self.P2(2*i+4)
        return int(r)

    #Calculates the nth stairsum
    def NG(self, n):
        return(n*2+4)

    #Calculates the stairsum g for the nth Pstair
    def SNP(self, n):
        k=1
        while(self.tz(k)<n):
            k=k+1
        return self.NG(k)

    #calculates how many stairsums occur up to a given g (including stairsum for g)
    def SBG(self, g):
        n=1
        while(self.NG(n)<g):
            n=n+1
        return n

    #Calcs l of the nth PStair.
    def LONP(self, n):
        g=self.SNP(n)
        #print("Stairsum =",g)
        rpos=self.P2(g)
        #print("Number of stairs with that stairsum p =", rpos)
        m=int((g-4)/2) #calculate how many times d=l for a given g
        #print("Position within that stairsum range rpos =", rpos)
        #print("m =", m)
        tpos = self.tz(self.SBG(g))#n+rpos-1
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
    def AINC(self, p):
        n=1000000000
        c=0
        for i in range(1,n+1):
            for k in range(1,i+1):
                c+=1
                if(c==p):
                    return i+2

         
    #calcs a of the nth pstair
    def A_of_NP(self, n):
        g=self.SNP(n)
        rpos=self.P2(g)
        tpos = self.tz(self.SBG(g)-1)+1
        #print("rpos,tpos,",rpos,tpos)
        return(self.AINC(n-tpos+1))

    #calcs b of the nth pstair
    def B_of_NP(self, n):
        a=self.A_of_NP(n)
        g=self.SNP(n)
        return int(((g+4)/2)-a)

    # returns 2,2,3,2,3,4,2,3,4,5,2...
    def CINC(self, p):
        n=100000000
        c=0
        for i in range(1,n+1):
            for k in range(1,i+1):
                #print(i,k)
                c+=1
                if(c==p):
                    return k+1

    #calcs c of the nth pstair
    def C_of_NP(self, n):
        g=self.SNP(n)
        rpos=self.P2(g)
        tpos = self.tz(self.SBG(g)-1)+1
        #print("tpos=",tpos)
        return(self.CINC(n-tpos+1))

    #calcs d of the nth pstair
    def D_of_NP(self, n):
        a=self.A_of_NP(n)
        b=self.B_of_NP(n)
        c=self.C_of_NP(n)
        return a+b-c

    #calculate and print the nth pstair
    def PStair_nth(self, n):
        self.a=self.A_of_NP(n)
        self.b=self.B_of_NP(n)
        self.c=self.C_of_NP(n)
        self.d=self.a+self.b-self.c
        self.g=self.SNP(n)
        self.l=self.LONP(n)

    def __init__(self, n):
        self.valid=False
        if (isinstance(n, int)==True and n>0):
            self.PStair_nth(n)
            self.valid=True
