
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
