
'''
import itertools
l1=["ha","sa"]
l2=["di","fe"]
l=[l1,l2]
f=["{} {}".format(*i) for i in itertools.product(*l,repeat = 1)]
print(f)
'''
def roman( num):
    M=[" ","M","MM","MMM"]
    C=[" ","C","CC","CCC"]
    X=[" ","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    I=[" ","I","II","III","IV","V","VI","VII","VIII","XI"]
    T=M[num/1000]
    H=C[(num%1000)/100]
    TEN=X[(num%100)/10]
    one=I[num%10]

    a=(T+H+TEN+one)
    return a
num=3549
print(roman(3549))
    
