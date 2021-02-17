# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:00:27 2021

@author: Windows10
"""

# initialise months
months = 0

# initialise current savings
current_savings = 0

# down payment is 0.25 of the total cost of the house
portion_down_payment = 0.25

# investment return of 0.04
r = 0.04

# prompt user input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# down payment is 0.25 of the total cost
down_payment = total_cost*portion_down_payment

# loop until enough savings for down payment
while current_savings < down_payment:
    
    # calculate monthly salary from annual salary
    monthly_salary = annual_salary/12
    
    add_savings = current_savings*r/12
    current_savings += (portion_saved * monthly_salary) + add_savings
    
    if months > 0 and months % 6 == 0:
        annual_salary *= (1+semi_annual_raise)
    
    months += 1

print("Number of months: " + str(months))