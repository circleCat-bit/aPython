import sys
import pyperclip
password = {"themanwhosenameisblanking@gmail.com" : "Meomeomeo123!",
            "24103624@phenikaa-uni.edu.vn": "Meomeomeo123!",
            "mimimi@lukas.com": "Mitsubishi1"}
def main():
    if len(sys.argv) > 2:
        print("ArgvError: too many arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("ArgvError: Too few arguments")
        sys.exit()
    else:
        account = sys.argv[1]
        if account not in password.keys():
            print(f"Can't find account named {account}")
        else:
            pyperclip.copy(password[account])
if __name__ == "__main__":
    main()
            
