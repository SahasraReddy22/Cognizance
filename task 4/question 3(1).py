#this program is to make a 2D list of voters in different cities and their phone numbers
persons=[
  ['a00','a01','a02'],
  ['a10','a11','a12'],
  ['a20','a21','a22']
]
for r in range(3):
  persons[r][0]=input('enter the name ')
  persons[r][1]=input('enter the number ')
  persons[r][2]=input('enter the city ')
print('name','number','city')
for person in persons:
  print(person[0],(6-len(person[0]))*" ",person[1],(6-len(person[1]))*" ", person[2])
    