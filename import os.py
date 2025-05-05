import os
import getpass

file_path = "data.txt"

currrent_user = getpass.getuser()

if os.path.exists(file_path):
    if current_user == "admin":
        print("FILE EXIST")
        with open(file_path, "r") as file:
            content = file.read()
            print(content)

    else:
        print("ACESS DENIED")

else: 
    print("FILES DOES NOT EXIST")