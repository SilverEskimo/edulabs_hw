tax_rate1 = 0.1
tax_rate2 = 0.14
tax_rate3 = 0.2
tax_rate4 = 0.31
tax_rate5 = 0.35
tax_rate6 = 0.47
tax_rate7 = 0.5

income_level1 = 77400
income_level2 = 110880
income_level3 = 178080
income_level4 = 247440
income_level5 = 514920
income_level6 = 663240

income = int(input("Please enter your annual salary: "))
total_tax = 0

# <= 77400
if income <= income_level1:
    total_tax += income * tax_rate1
# <= 110880
elif income_level1 < income <= income_level2:
    total_tax += (income_level1 * tax_rate1) + (income - income_level1 + 1) * tax_rate2
# <= 178080
elif income_level2 < income <= income_level3:
    total_tax += income_level1 * tax_rate1 + income_level2 * tax_rate2 + (income - income_level2 + 1) * tax_rate3
# <= 247440
elif income_level3 < income <= income_level4:
    total_tax += income_level1 * tax_rate1 + income_level2 * tax_rate2 + income_level2 * tax_rate3 + \
                 (income - income_level3 + 1) * tax_rate4
# <= 514920
elif income_level4 < income <= income_level5:
    total_tax += income_level1 * tax_rate1 + income_level2 * tax_rate2 + income_level2 * tax_rate3 + \
                 income_level3 * tax_rate4 + (income - income_level4 + 1) * tax_rate5
# <= 663240
elif income_level5 < income <= income_level6:
    total_tax += income_level1 * tax_rate1 + income_level2 * tax_rate2 + income_level2 * tax_rate3 + \
                 income_level3 * tax_rate4 + income_level4 * tax_rate5 + (income - income_level5 + 1) * tax_rate6
else:
    total_tax += income_level1 * tax_rate1 + income_level2 * tax_rate2 + income_level2 * tax_rate3 + \
                 income_level3 * tax_rate4 + income_level4 * tax_rate5 + income_level5 * tax_rate6 + \
                 (income - income_level6 + 1) * tax_rate7

print(f"The total tax you'll pay is: {total_tax} NIS")