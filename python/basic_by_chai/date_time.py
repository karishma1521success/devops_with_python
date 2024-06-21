from datetime import date
# Extract today date
today = date.today()

if today.weekday() == 0:
    print("Today is: Monday")
elif today.weekday() == 1:
    print("Today is: Tuesday")
elif today.weekday() == 2:
    print("Today is: Wednesday")
elif today.weekday() == 3:
    print("Today is: Thursday")
elif today.weekday() == 4:
    print("Today is: Friday")
elif today.weekday() == 5:
    print("Today is: Saturday")
else:
    print("Today is: Sunday")