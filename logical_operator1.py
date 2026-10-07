# logical operator = evaluate multiple condition (or, and, not)
                # or = at least one condition ms be true
                # and = both condition must be true
                # not = inverts the condition

temp = 44
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is on schedule")