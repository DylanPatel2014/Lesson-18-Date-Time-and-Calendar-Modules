import calendar
year=int(input("Please write the year you want to see the calendar of:"))
month=1
for i in range (12):
    print(calendar.month(year,month))
    print("The month's number in the year is",month,end=(""))
    month= month +1
    