annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved
current_savings = 0.0
months = 0
while current_savings < down_payment:   
    months += 1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit    
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_deosit = monthly_salary * portion_saved
    
print('Number of months:', months)