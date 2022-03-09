import numpy as np
#user inputing  the elements of 1st array
elements1=int(input("enter the no.of elements of 1st array "))
a=np.zeros(elements1)
u=len(a)
i=0
while i<u:
  x=int(input("enter the element "))
  a[i]=x
  i+=1
print(a)
#user inputing the elements of 2nd array
elements2=int(input("enter the no.of.elements of 2nd array "))
b=np.zeros(elements2)
v=len(b)
j=0
while j<v:
  y=int(input("enter the element "))
  b[j]=y
  j+=1
print(b)
#checking if arrays are equal
print(np.array_equal(a,b))
