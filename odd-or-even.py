#Odd or Even
num = int(input('Enter a number: '))

result = num % 2
result_4 = num % 4 == 0

if(result_4):
  print('This number is a multiple of 4')
elif(result == 0):
  print('This number is Even')
else:
  print('This number is Odd')