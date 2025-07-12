import pprint
message = input("Enter your message: ")
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1

print(count)
print("The difference: ")
pprint.pprint(count)