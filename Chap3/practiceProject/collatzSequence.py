#collatz function
def collatz(num):
    if (num % 2 == 0):
        newNum = num // 2
    else:
        newNum = num * 3 + 1
    return newNum

#program
num = 0
while (True):
    try:
        num = int(input("Enter number: "))
        break
    except ValueError:
        print("Enter a valid number")
        continue
    
result = collatz(num)
print("Collatz Sequence: ")
print(result)
while (result != 1):
    result = collatz(result)
    print(result)
print("Done")    
