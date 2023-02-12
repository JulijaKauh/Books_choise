import datetime
#Project starts:
print("When does your project start: ")
year1 = int(input("Year: "))
month1 = int(input("Month: "))
day1 = int(input("Day: "))
#Project ends:
print("When does your project end: ")
year2 = int(input("Year: "))
month2 = int(input("Month: "))
day2 = int(input("Day: "))
#amount of days between them
start_project = datetime.date(year1, month1, day1)
end_project = datetime.date(year2, month2, day2)
count_of_days = start_project - end_project
print("Start: {}. Ends {}. It takes {} day/s.".format(start_project, end_project, abs(count_of_days.days)))
