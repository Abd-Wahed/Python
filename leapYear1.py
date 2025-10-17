year = input("Enter a year: ")
year = int(year)
if year % 100 !=0 and year %4 ==0:
    print("Yes")
elif year %100 ==0 and year %4 ==0:
    print("Yes")
else:
    print("No")
