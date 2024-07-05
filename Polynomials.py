from math import sqrt
import numpy as np
from matplotlib import pyplot as plt


def splitbysigns(s):
    if not isinstance(s, str): raise TypeError
    if not s:   return []
    
    if not s[0] in {'+', '-'}:
        s= '+' +s
    dL= []
    i= -1
    for ch in s:
        if ch in {'+', '-'}:
            i+= 1
            dL.append('')
        dL[i]+= ch
        
    return dL
sbs= splitbysigns


'''The construction
7..5—Basic methods.     #...
    3—Management.
    3—Getting info.
7—Operators/function handling.      #Topic to end.
    5—Other basical.
    5—Mathematical operators.
7..5—Mathematical analises/calculations.    #Code block the CAN be developed.
7..3—Initialization.    #Topic virtually closed.
    2—__init__'''



#class list(list):   pass    #—Abstracting list. :)  #—Still no effect :(
class polynomial(list):
    '7..5−Basic methods.-----------------------------'
    '3—Management'
    '2−...'
    def optimise(s3):
            while s3 and s3[-1]==0:      s3.pop(-1)



    '2−...'
    def extended(s3, iterable):
        return  list(iterable) +s3



    '2−...'
    copy= lambda s3: polynomial(s3)
    
    
   

   
    '3−Getting info'
    '2−Calculating polynomial\'s degree'
    d= degree= property(lambda s3: len(s3) -1)
    









    '7-Operations / operator handling---------------------------'
    '5-3−Iterations'
    '2-...'
    def __iter__(s3):
        s3.i= len(s3)
        return  s3



    '2-...'
    def __next__(s3):
        s3.i-= 1
        if s3.i<0: raise StopIteration
        return  s3[s3.i]






    '5−Casting'
    '3-Str representation'
    Pow_r= {1: "",}
    Pow_r.update( ((i, l) for i,l in enumerate("²³⁴⁵⁶⁷⁸⁹", 2)) )
    '2−__str__'
    def __str__(s3, variable= "x"):
        if not s3:    return "0"
        
        v= variable
        
        line= ""
        degree= s3.d
        for c in s3:
            if c==0:    continue
            #1−Spacing
            line+= " "
            #1−Coefficient
            s= format(c, "+")
            line+= s
            
            #1−Variable
            #if issubclass(type(v), int, float, complex):  line+= "*"
            if degree>0:
                #−Correction
                if abs(c)==1: line= line[:-len(s)+1]

                #0−Variable
                s= str(v)
                if s.isidentifier():
                    line+= s
                else:
                    line+= "(" +s +")"
                #1−Exponent
                if degree in s3.Pow_r:
                    line+= s3.Pow_r[degree]
                else:   line+= "^%s"%degree     #−For higher powers
                
                degree-= 1

        #—Fixing text line
        line= line[1:]
        if line[0]=='+':    line= line[1:]

        return line



    '2−__repr__'
    def __repr__(s3):
        s= ", ".join((str(c) for c in s3))
        return "polynomial([%s])"%s





    #3−Collections
    #2−__list__
    
    
    
    #2−__tuple__


    #3−Management
    def __lshift__(s3, n):
        return  s3 +[0]*n


    def __rshift__(s3, n):
        if n>= len(s3): return polynomial()
        y= s3.copy()
        while n:
            y.pop(0)
            n-= 1
        return  y






    
    '5-Mathematical operations'
    '3−Summing'
    '2−__add__'
    def __add__(s3, ex):
        '0−For number'
        if isinstance(ex, (int, float, complex)):
            P= s3.copy()
            P[0]+= ex
            P.optimise()
            return P   #−Optimised


        '0−For polynomial.'
        if isinstance(ex, (polynomial,)):
            '0−Asigning'
            if s3.d > ex.d:
                a, b= s3, ex
            else:  a, b= ex, s3
            y= a.copy()
            
            '0−Summing coefficients.'
            i= 0
            for c in b:
                y[i]+= b[i]
                i+= 1

            '0−Returning'
            y.optimise()   #−Optimised
            return y


        if isinstance(ex, (list)):
            return  polynomial((list(s3) +ex)) #−Initialized



    '2−__radd__'
    def __radd__(s3, ex):
        #1−__add__
        if isinstance(ex, (int, float, complex, polynomial,)):
            return s3 +ex   #−__ladd__ in use
        if isinstance(ex, (list)):
            return  polynomial((ex +list(s3))) #−Initialized



    '2—__sub__'
    def __sub__(s3, ex):
        return s3 +(-1)*ex



    '2−__rsub__'
    def __rsub__(s3, ex):
        return ex +(-1)*s3





    '3−Multiplying'
    '2—Multiplication'
    def __mul__(s3, ex):
        if isinstance(ex, (int, float, complex)):
            P= s3.copy()
            for i in range(len(P)):    P[i]*= ex
            P.optimise()    #−Optimised
            return P
        if isinstance(ex, (polynomial,)):
            #print(s3, ex,'\n',sep='\n')
            y= 0
            for i in range(len(ex)):
                #print("Creating",t)
                y+= s3*ex[i]<<i
                #print("Adding",y)
            return y

    
    
    __rmul__= __mul__
    


    '2—__truediv__'
    def __truediv__(s3, ex): 
        if isinstance(ex, (int, float, complex)):
            P= s3.copy()
            for i in range(len(P)):    P[i]/= ex
            P.optimise()    #−Optimised
            return P

        if isinstance(ex, (polynomial,)):  
            return RE(s3, ex)



    '2−__rtruediv__'
    def __rtruediv__(s3, ex):
        return RE(ex, s3)


    
    '2—__floordiv__'
    def __floordiv__(s3, ex):
        if isinstance(ex, (int, float, complex)):
            P= s3.copy()
            for i in range(len(P)):    P[i]//= ex
            P.optimise()    #—Optimised
            return P
    
    
    '2—__rfloordiv__'
  




    '3—Assigning'
    '2—__iadd__'
    __iadd__= __radd__
        
    
    '2—__imul__'
    __imul__=  __mul__
        
    
    
    
    
    
    '3—Plus & minus operators'
    __pos__= lambda s3: s3
    __neg__= lambda s3: -1*s3
    
    
    
    




    '7..5—Mathematical analises/calculations--------------'
    '3—Horner & his children'
    '2—Horners algorithm.'
    def horne(s3, x):
        y= 0
        L= []
        for c in s3:
            y*= x
            y+= c
            L.append(y)

        return polynomial(L[:-1]), y
    
    
    
    '2—Computing polynomial value for given x.'
    def __call__(s3, x):
        if issubclass(type(x), (int,float,complex)):
            return s3.horne(x)[1]
        else:
            return s3.__str__(x)





    
    '3—Analis'
    '2—For quadratic function'
    Quadratic= {
        "cΔ": lambda P:     P[1]**2 -4*P[0]*P[2],
        "xv": lambda P:     -P[1]/(2*P[2]),
        "yv": lambda P, Δ:  -Δ/(4*P[2]),
        "x1": lambda P, Δr: (-P[1] -Δr)/(2*P[2]),
        "x2": lambda P, Δr: (-P[1] +Δr)/(2*P[2]),
        }



    '2—Deriviative'
    def deriviative(s3, order= 1):
        if type(order)!=int or order<0:
            raise TypeError("Sorry, I can't deriviate deriviative of order %r."%order)

        P= s3.copy()
        while order:
            d= 1; stop= len(P)
            while d<stop:
                P[d-1]= P[d]*d
                d+= 1
            order-= 1
            if len(P):  P.pop(-1)   #—Cheaper alternative for .optimise()!!!
            else:   break

        return P
        

    der8= deriviative    
    
    
    
    def plot(s3, show= True, save= {}):
        d= s3.d
        if d in {-1, 0}:
            aX= np.array(range(-5,6))
        elif d in {1, 2}:
            Zp= s3.fzp()    #float
            
            if d==1:    mid= Zp[0]
            else:   mid= polynomial.Quadratic["xv"](s3)
            
            if len(Zp) in {0,1}:
                aX= np.array([i+mid for i in range(-5,6)])   #10 real num._
            else:
                step= abs(Zp[0] -Zp[1])/6
                R4= range(-2,3)
                
                aX= [i*step+Zp[0] for i in R4] +[mid] +[i*step+Zp[1] for i in R4]    #11
                aX= np.array(aX)
        else:
            raise NotImplementedError("Sorry, I cannot plot a graph for polynomial,"
                            +" which has degree equal to %i."%d)
  
        
        aY= np.array([s3(x) for x in aX])
                    
        
        o= plt.plot(aX, aY)
        plt.grid(axis= "both", color= "black", lw= 0.3)
        if save:    plt.savefig(**save)
        if show:    plt.show()
        
        return o
        
        
    
    
    
    
    
    '3—Finding zero places'
    '2—Defining zero place seekers'
    def fzp_2(s3):
        Q= polynomial.Quadratic
        Δ= Q["cΔ"](s3)

        if Δ<0:     return []
        if Δ==0:    return [Q["xv"](s3)]
        
        Δr= sqrt(Δ)
        Zp= [Q["x1"](s3, Δr), Q["x2"](s3, Δr)]
        Zp.sort()
        return Zp
    
    
    Zp_seekers= {
            -1: lambda *args: "R",
            0:  lambda *args: [],
            1:  lambda P: [-P[0]/P[1]],
            2:  fzp_2,
        }
    del fzp_2
    
    
    
    '2—Official zero place seeker.'
    def find_zero_places(s3):  ###Upgrade for better ...
        d= s3.d
        if d in range(-1, 3):
            return polynomial.Zp_seekers[d](s3)

        print("Sorry, but I cannot find zero places for polynomial of %i degree."%d) 

    fzp= find_zero_places

    
    
    
    
    
    
    '7—Initialization-----------------------'
    def str2plist(s):
        s= s.replace(' ', "")
        dL= splitbysigns(s) #Contains all terms
        dMo_= set() #Monomials

        for s in dL:
            Mo= {"sing": s[0], "coef": "", "var": "", "exp": "", "isexpcl": True}    #Monomial
            i= 0
            try:
                #0|For coefficient
                while s[i].isdigit() or s[i] in "./*":
                    Mo["coef"]+= s[i]
                    i+= 1
                #0|For variable
                while s[i].isalpha():
                    Mo["var"]+= s[i]
                    i+= 1
                #0|For exponent
                if s[i]=='^':   Mo["isexpcl"]= False
                while s[i].isnumeric():
                    Mo["exp"]+= s[i]
                    i+= 1
                raise Exception
            except IndexError:  #Unevitable & expected error
                #0|simplifications
                Mo["sign"]= True if Mo["sign"]=='-' else False
                Mo["coef"]= eval(Mo["coef"])
                if Mo.pop("isexpcl"):
                    Mo["exp"]= "²³⁴⁵⁶⁷⁸⁹".find(Mo["exp"])+2
                    #It may occur that Mo["exp"]==1. ⇔ It's ok.
                else: Mo["exp"]= int(Mo["exp"])
            finally:
                dMo_.add(Mo)
                
                
        raise NotImplementedError("Not finished.")
        
        
        
    def __init__(s3, ex= ()):
        if isinstance(ex, str):
            raise NotImplementedError
            ex= []
        if hasattr(ex, "__iter__"):
            super().__init__(ex)
            s3.reverse()
        else:   raise TypeError('%s is invalid type for parameter "ex".'%type(ex))
        s3.optimise()



pol= polynomial







'7—Avoiding inheritance'     #Not working.
Ra= Redundant_attr= ("__gt__", "__lt__", "__ge__", "__le__") #5-1—Inequalities.
#for attr in Ra: delattr(polynomial, attr)
del Ra, Redundant_attr
