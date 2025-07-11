birthdays = {"Alice": "April 1", "Hummle" : "March 20", "Buck": "September 12", "Don": "January 2"}
while True:
    name = input("What's the name? ")
    if not name:
        print("Quit")
        break
    elif name in birthdays:
        print("Birthday of " + name + " is" + birthdays[name])
    elif name not in birthdays:
        print(name + " is not in bir database")
        while True:
            add = input("Do you want to add this person's birthday? (y or n): ")
            if (add == 'y' or add == 'Y'):
                bd = input("Enter birthday: ")
                birthdays[name] = bd
                print("Data's added successfully")
                break
            elif (add == 'n' or add == 'N'):
                print("OK. Don't add")
                break
            else:
                print("You must enter a valid character!!!")
                continue
        