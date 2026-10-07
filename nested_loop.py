# nested loop = A loop with another loop

rows = int(input("Enter the number to use:"))
colums = int(input("Enter the number to use"))
symbols = input("Enter the symbol to use:")

for x in range(rows):
    for y in range(colums):
         print(symbols, end= "")
    print()