cat_names = []
while True:
    cat = input("cat's name: ")
    if (not cat):
        break   
    cat_names.append(cat)
for cat in cat_names:
    print(cat)