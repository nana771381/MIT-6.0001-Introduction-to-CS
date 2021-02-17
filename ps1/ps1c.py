# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:07:53 2021

@author: Windows10
"""

steps = 0
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost

# searching for best rate between 0.00% to 100.00%
high = 10000
low = 0

# limit of accuracy
epsilon = 100

starting_salary = int(input("Enter the starting salary: "))


while True:
    portion_saved = (high + low)/2
    annual_salary = starting_salary
    current_savings = 0
    
    # to calculate your savings after 36 month based on the different saving rate
    for months in range(36):
        
        # calculate monthly salary from annual salary
        monthly_salary = annual_salary/12
    
        add_savings = current_savings*r/12
        current_savings += float((portion_saved * monthly_salary)/10000) + add_savings
        
        if months > 0 and months % 6 == 0:
            annual_salary *= (1+semi_annual_raise)
                    
            
    if abs(current_savings - portion_down_payment) < epsilon:
        print("Best savings rate:", '%.4f' %(portion_saved/10000))
        print("Steps in bisection search: ", steps)
        break
        
    # saved too much, decrease portion_save
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
        high = portion_saved
        
    # saved too little, increase portion_save
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
        low = portion_saved
    
    if low == high:
        print("It is not possible to pay the down payment in three years.")
        break
    
    steps += 1