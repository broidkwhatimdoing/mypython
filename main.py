
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

def greet(first_name, last_name):
  print(f"Hi {first_name}, {last_name}")
  print("Welcome Aboard")
greet("Allison", "Zeng")

def get_greeting(name):
  return f"Hi {name}"


message = get_greeting ("Allison")
file = open("content.txt", "w")
file.write(message)

def increment(number, by):
  return number + by
print(increment(2, 5))

def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
    return total
print(multiply(2,3,4,5))

print("Hello World")
print("@"*10)
print(2+6)

message = """blah, blah, blah"""

print(message)
print(len(message))

print(message[1])
print(message[-1])
print(message[0:4])

course = "python \"programing"
print(course)

first = "Allison"
last = "Zeng"
full_name = first + " " + last
print(full_name)

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
  print("Eligible")

age = 22
if age >= and age < 65:
  print("Eligible")


print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("ing"))
print(course.replace("ing" , "poop"))
print("pro" in course)
print("poop" in course)



# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

course = "python programming"
print("swift" not in course)

print(10 // 3)
print(10 % 3)
x = 10
x = x + 3
x += 3
print(x)
print(round(5.93939475))

input("x:")
y = int(x) + 1
print(f"x: {x}, y: {y}")

input("temperature:")
if input > 30:
  print("It's warm")
  print("Drink water")
elif input > 20:
  print("It's nice")
else:
  print("It's Cold")
print("Done")
