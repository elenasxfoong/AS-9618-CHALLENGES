import datetime

year = int(input("Enter the year of your project: "))

month = int(input("Enter the month of your project: "))

date = int(input("Enter the date of your project: "))

x = datetime.datetime.now()
y = datetime.datetime(year, month, date)
print ("Today's date:" , x)
print("Project due:" ,y)

timediff = y - x
print ("Days left until project is",timediff)
