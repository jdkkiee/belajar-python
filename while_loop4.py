num = int(input("Enter Number (Between 1 - 10):"))

while num < 1 or num > 10:
    print(f"{num} is nor valid")
    num = int(input("Enter Number (Between 1 - 10):"))
print(f"Your number is {num}")