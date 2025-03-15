no_of_days = int(input())
years = no_of_days//365
rem=no_of_days%365
weeks= rem//7
rem=no_of_days%7
print("years:",years)
print("weeks:",weeks)
print("days:",rem)