from os import _exit as exit

#
# Author: Firedorange717
#   Description: A program collects your spendings throughout the year and shows you where you are spending
#                  your money.


#Sets up title
print('-'*29)
print('-'*5,'WHERE\'S THE MONEY','-'*5)
print('-'*29)


#Checking for Valid inputs
annualSalary = input('What is your annual salary? \n' )

if annualSalary.isnumeric() != True:
    print('Must enter positive integer for salary.')
    exit(0)
else:
    monthlyMortgage = input('How much is your monthly mortgage or rent? \n')

annualSalary = int(annualSalary)

if monthlyMortgage.isnumeric() != True:
    print('Must enter positive integer for mortgage or rent.')
    exit(0)
else:
    bills = input('What do you spend on bills monthly? \n')

monthlyMortgage = int(monthlyMortgage)

if bills.isnumeric() != True:
    print('Must enter positive integer for bills.')
    exit(0)
else:
    weeklyExpenses = input('What are your weekly grocery/food expenses? \n')

bills = int(bills)

if weeklyExpenses.isnumeric() != True:
    print('Must enter positive integer for food.')
    exit(0)
else:
    annualTravel = input('How much do you spend on travel annually? \n')

weeklyExpenses = int(weeklyExpenses)

if annualTravel.isnumeric() != True:
    print('\nMust enter positive integer for travel.')
    exit(0)
else:
    print('\n')
annualTravel = int(annualTravel)


# Determining Tax Bracket
if annualSalary > 200000:
    tax_Percentage = 30
elif annualSalary > 75000:
    tax_Percentage = 25
elif annualSalary >15000:
    tax_Percentage = 20
else:
    tax_Percentage = 10

finalTax = annualSalary * (tax_Percentage / 100.0)

if finalTax >= 50000:
    finalTax = 50000



# Multipliy variables to equate to year total
monthlyMortgage = monthlyMortgage * 12
bills = bills * 12
weeklyExpenses = weeklyExpenses * 52

#Determine extra money
extra = annualSalary - (monthlyMortgage + weeklyExpenses + bills + annualTravel + finalTax)


deficit = int(float(extra))
taxLimit = int(float(finalTax))



# calculating Percentages
monthlyMortgagePercent = monthlyMortgage / annualSalary * 100
billsPercent = bills /annualSalary *100
weeklyExpensesPercent = weeklyExpenses / annualSalary * 100
annualTravelPercent = annualTravel / annualSalary * 100
extraPercent = extra / annualSalary * 100


# Hashtag graph showing
mortgageHash = int(monthlyMortgagePercent)
billsHash = int(billsPercent)
weeklyHash = int(weeklyExpensesPercent)
travelHash = int(annualTravelPercent)
taxHash = int(tax_Percentage)
extraHash = int(extraPercent)

dashes = max(mortgageHash,billsHash,weeklyHash,travelHash,taxHash,extraHash)



#Money Decimal Conversion
annualSalary = str(annualSalary)
monthlyMortgage = format(monthlyMortgage, '10,.2f')
bills = format(bills, '10,.2f')
weeklyExpenses = format(weeklyExpenses, '10,.2f')
annualTravel = format(annualTravel, '10,.2f')
finalTax = format(finalTax, '10,.2f')
extra = format(extra, '10,.2f')



#Percent Decimal Conversion
monthlyMortgagePercent = str(format(monthlyMortgagePercent, '5.1f'))
billsPercent = str(format(billsPercent, '5.1f'))
weeklyExpensesPercent = str(format(weeklyExpensesPercent, '5.1f'))
annualTravelPercent = str(format(annualTravelPercent, '5.1f'))
tax_Percentage = str(format(tax_Percentage, '5.1f'))
extraPercent = str(format(extraPercent, '5.1f'))



#Displaying the data
print('-'*42 + '-'*dashes)
print('See the financial breakdown below, based on a salary of','$'+ annualSalary)
print('-'*42 + '-'*dashes)
print('| mortgage/rent |' , '$' , monthlyMortgage, '|' , monthlyMortgagePercent + '%' , '|' , '#'* mortgageHash)
print('|         bills |' , '$' , bills, '|' , billsPercent + '%' , '|' , '#'* billsHash)
print('|          food |' , '$' , weeklyExpenses, '|' , weeklyExpensesPercent + '%' , '|' , '#'* weeklyHash)
print('|        travel |' , '$' , annualTravel, '|' , annualTravelPercent + '%' , '|' , '#'* travelHash)
print('|           tax |' , '$' , finalTax, '|' , tax_Percentage + '%' , '|' , '#'* taxHash)
print('|         extra |' , '$' , extra, '|' , extraPercent + '%' , '|' , '#'* extraHash)
print('-'*42 + '-'*dashes)

#Displays defecit and tax limit if triggered
if deficit < 0:
    print('>>> WARNING: DEFICIT <<<')

if taxLimit == 50000:
    print('>>> TAX LIMIT REACHED <<<')
