#converting 1st character of each element to uppercase
import pandas as pd
words=pd.Series(['amrita','school','of','engineering','chennai','campus'])
uppercase=words.str.title()
print(uppercase)
 


  
  


    