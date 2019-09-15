annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, in decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0
while current_savings < portion_down_payment:
    current_savings += (annual_salary/12)*portion_saved + current_savings*(r/12)
    months += 1
print("Number of months to saved: ", months)