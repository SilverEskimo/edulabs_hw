# # Annual income tax calculation
# salary = int(input("Insert you salary: "))
#
# total_tax = 0
#
# if salary > 0:
#     salary_for_stage = min(salary, 77400)
#     total_tax += salary_for_stage * 0.1
# if salary > 77400:
#     salary_for_stage = min(salary, 110880)
#     total_tax += (salary_for_stage - 77401) * 0.14
# if salary > 110880:
#     salary_for_stage = min(salary, 178080)
#     total_tax += (salary_for_stage - 110880) * 0.2
# if salary > 178080:
#     salary_for_stage = min(salary, 247440)
#     total_tax += (salary_for_stage - 178080) * 0.31
# if salary > 247440:
#     salary_for_stage = min(salary, 514920)
#     total_tax += (salary_for_stage - 247440) * 0.35
# if salary > 514920:
#     salary_for_stage = min(salary, 663240)
#     total_tax += (salary_for_stage - 514920) * 0.47
# if salary > 663240:
#     total_tax += (salary - 663240) * 0.5
# print(f"Your annual tax is: {total_tax}")

salary_levels = [77400, 110880, 178080, 247440, 514920, 663240]
tax_levels = [0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5]


def calc_tax(salary: float) -> float:
    print("aaa")
