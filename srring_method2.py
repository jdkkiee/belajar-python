username = input("Enter your Username:")

if len(username) > 12:
    print("Your username can't be more than 12!")

elif not username.find (" ") == -1:
    print("Your username can't contain space!")

elif not username.isalpha():
    print("Your username can't contain number!")

else:
    print(f"Welcome {username}")