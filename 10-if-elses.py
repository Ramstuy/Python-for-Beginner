dud = True
height = False

if dud == True and height == True:
# if = jika
    print('Dud is a dude or He got a body height')
elif dud == False and height == False:
# elif bisa juga ditulis else if
    print('Not a dude or Doesn'+"'"+'t have a body height')
else: 
# else = jikalau tidak
    print('Unknown entity')

# =================================================================
# Berikut ini beberapa contoh code penggunakan if-else

value = int(input('Input value: '))

if value%5 == 0:
    print(value,'can be divided by 5')
else:
    print(value,'cannot be divided by 5')

# =================================================================

value = input('Input value: ')

if value<10:
    print(value,'is less than 10')
else:
    print(value,'is greater than 10')

# =================================================================

num = int(input('Enter a number: '))

if num%2 == 0:
    print(num,'is even')
else:
    print(num,'is odd')

# =================================================================
# Contoh code basic calculator menggunakan if-else

num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
opr = input('Enter Operation: ')

if opr == '+':
    print(num1 + num2)
elif opr == '-':
    print(num1 - num2)
elif opr == '/':
    print(num1 / num2)
elif opr == '*':
    print(num1 * num2)
else:
    print('Invalid operation')
    
# =================================================================