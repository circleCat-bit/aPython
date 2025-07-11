cat_names = ["Lil", "John", "Fang", "Mumle", "Jack", "Kiss"]
print("Enter nothing to exit")
flag = 'y'
while flag == 'y':
    cat_name = input("your cat's name: ")
    if not cat_name:
        break
    elif cat_name not in cat_names:
        print("There's no cat named " + cat_name)
        continue
    elif cat_name in cat_names:
        print("Here's your cat")
        while True:
            flag = input("Do you still want to find cat? (y or n): ")
            if (flag not in ['y', 'n', 'Y', 'N']):
                print("Please enter (y or n): ")
                continue
            elif flag == "Y":
                flag = "y"
            elif flag == "N":
                flag = "n"
            break
            
        
    