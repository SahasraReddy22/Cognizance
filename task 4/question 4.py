#program to check if a given number is palindrome
number= int(input('enter the number'))
i=number
reverse=0
while (i>0):
  remainder=i%10
  reverse=reverse*10+remainder
  i=i//10
if number==reverse:
  print('true')
else :
  print('false')
