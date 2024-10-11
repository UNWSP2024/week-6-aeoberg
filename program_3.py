# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program


def county_tax(sales):
    county = sales * 0.025
    return county

def state_tax(sales):
    state = sales * 0.05
    return state

if __name__ == '__main__':
    totalSales = int(input("What is the total sales? $"))
    totalCountyTax = county_tax(totalSales)
    totalStateTax = state_tax(totalSales)
    print('County Sales Tax: $',totalCountyTax)
    print('State Sales Tax: $',totalStateTax)
    entireTax = totalCountyTax + totalStateTax
    print('Total Sales Tax: $',entireTax)
