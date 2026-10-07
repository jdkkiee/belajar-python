weight = float(input("Enter your weight:"))
unit = input("Kilogram or Pounds (K/L):")

if unit  == "K":
    weight = weight * 2.205
    unit = "kbs."

elif unit == "L":
    weight = weight / 2.205
    unit = "pds."

else:
    print("Not define!")

print(f"Your weight is {round(weight, 1)} {unit}")