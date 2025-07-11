message = input("Enter your message: ")
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1
for k, v in count.items():
    print(f"{k}: {v}")