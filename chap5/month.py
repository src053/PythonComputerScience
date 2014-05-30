# This program will print the abbreviation of a month, given its number

def main():
	#List for main lookup table
	months = "JanFebMarAprMayJunJulAugSepOctNovDec"

	n = eval(input("Enter a month number (1-12): "))

	#Compute starting position of month n in months
	pos = (n-1) * 3

	#Grab the appropriate slice from months
	monthAbbrev = months[pos:pos+3]

	#Print the result
	print("The month abbreviation is", monthAbbrev + ".")

main()