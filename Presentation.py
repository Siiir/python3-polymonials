from math import pi
from Polynomials import *
#2|Statements
#1|Preperations
#0|Declaring collections with output
De= Descriptions= []
St= Statements= []

#0|Setting constants
De.append("Setting constants.")
St.append(("a= 5.8", "π= %r"%pi))

#0|Creating polynomials.
De.append("Declaring polynomials.")
St.append( ("W= polynomial([9.64,9.6])", "P= polynomial([1,2,1])", "Q= polynomial([2,3,4,5.0])", "R= polynomial()") )

#0|Creating rational expressions
#De.append("Declaring rational functions.")
#St+= ("F= RE(P, Q)",)

#0|Assigning & deleting
De.append( "Assigning & deleting" )
St.append( ("W[1]= 1; W[0]= 2", "R.append(1)", "R+= [5,6]", "R[::-1]= [4,5,6]",
 "R.pop(1)", "del R[0]", "R.clear()", "del R") )


#1|Outputting
assert len(De)==len(St)
print("Statements:".upper().ljust(50,'_'))
for de, st in zip(De, St):
    print()
    print( format(de, "-<40") )
    for s in st:
        print(s)
        exec(s)


#1-0|Clearing memory.
De.clear();     del St



#2|Expressions
#1|Preperations
#0|Declaring collections with output
#−De is still in game.
Ex= Expressions= []

#0|Presentation as string
De.append("Representation in string.")
Ex.append( ("W","P", "Q") )

#0|Computing polynomial value for constants.
De.append("Computing polynomial value for constants.")
Ex.append(("W(10)","P(a)","Q(π)"))

#0|Artmetic operations on polynomials.
De.append("Artmetic operations on polynomials.")
Ex.append(("+P","-Q", "W +10", "17.0 -P", "Q -17.7", "P +Q", "Q -W",
"-1*P", "Q*2.5", "Q*P", "W*P", "W/2.879", "Q//3",#Q/P, P//W
))

#0|Analising polynomials
De.append("Analising polynomials.")
Ex.append(("Q.degree", "W.d", "P.find_zero_places()", "W.fzp()"))

#0|Management
De.append("Management operations on polynomial objects.")
Ex.append(( "P<<5", "Q>>2", "W>>6", "[0,6] +P +[6,7,0]", "[9] +Q" ))

#0|Casting
#"repr(P)"


#1|Outputting
assert len(De)==len(Ex)
print("\n\n\n")
print("Expressions:".upper().ljust(50,'_'))
print("{: <20s}\t{:s}".format("Expression","Output"))
for de, ex in zip(De, Ex):
    print()
    print(format(de, "-<40"))
    for el5 in ex:
        print(el5.ljust(20), eval(el5), sep= "\t")



#1-0|Clearing memory.
del De, Ex
