
_ = round(4*3.751)
print(_)
print(spam)

print("This is Allison")

text = "# is not a comment because it's inside quotes."
print(text)

spam=11
scam=25
total=spam+scam
print(total)

spam=50-5*2
print(spam)

print(17/3)
print(17//3)
print(17%3)
print(2**7) 


# 2025/7/10
x=int (input("please enter an integer:"))
if x<10 : print('single')
if 100>x>9: print('double')
if 1000>x>99:print('triple')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
users['Éléonore']='unknown'
print(users['Éléonore'])
#del users['Hans']
users['Allison']= 'half-active'
print(len(users))
print(users)
users['Allison']= 'semi-active'
print(users)

a = sum(range(1,10))
print(a)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for number in range(1, 10, 4):
  print("Attempt", number, number * ".")

successful = True
for number in range(3):
  print("Attempt")
  if successful:
    print("Successful")
    break
else:
  print("Attempted 3 times and failed")

for x in range(5):
  for y in range(3):
    print(f"({x},{y})")

print(type(5))
print(type(range(5)))

for x in "Python":
  print(x)

for x in [1, 2, 3, 4]:
  print(x)

number = 100
while number > 0:
  print(number)
  number //= 2

command = ""
while command.lower() != "quit":
  command = input (">")
  print("ECHO", command)




