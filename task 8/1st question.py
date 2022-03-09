#building a new vector with 5 consecutive zeros interleaved between each value
import numpy as np
vector=np.array([10,11,12,13,14])
p=5
output=np.zeros(len(vector)+(len(vector)-1)*(p))
output[::p+1]=vector
print(output)                  
 


  
  


    