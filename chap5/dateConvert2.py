#Converts day month and year numbers into two date formats

def main():
	#get the day mont and year
	day, month, year = eval(input("Enter the day, month, and year numbers: "))

	date1 = "{0}/{1}/{2}".format(month,day,year)

	months = ["January", "February,", "March", "April", "May", "June", "July", "August", "September", "October",
			   "November", "December"]

	monthStr = months[month-1]
	date2 = "{0} {1}, {2}".format(monthStr,day,year)

	print("The date is", date1, "or", date2 + ".")

main()