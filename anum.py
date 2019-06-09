import time
import math
from tabulate import tabulate
n=eval(input("Enter the value of n: "));
t1=time.time()
a=2**n
t2=time.time()
A=t2-t1
t3=time.time()
b=n
t4=time.time()
B=t4-t3
t5=time.time()
c=n**2
t6=time.time()
C=t6-t5
t7=time.time()
d=math.log10(n);
t8=time.time()
D=t8-t7
t9=time.time()
e=n*math.log10(n);
t10=time.time()
E=t10-t9

print(tabulate([['n',b,A], ['logn',d,B], ['nlogn',e,C], ['n**2',c,D], ['2**n',a,E]], headers=['Function', 'Value', 'Time']))
templist= [A,B,C,D,E]
print(sorted(templist,key=int)) 
