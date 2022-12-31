#Write a program that helps people who look for a new job.
#The program receives the user's current monthly salary and a new job’s monthly salary.
#The program will calculate what is the difference of the annual salary between
#the old job and the new job, and will print the difference.
#For example, if currently I earn 8000 per month, and I consider taking a new job where I will earn 15000 per month,
#the program should print the following: “If you take the new job, you will earn 84000 more per year”

current_salary = int(input("Please enter your current salary: "))
new_salary = int(input("Please enter your new salary: "))
print(f'If you take the new job, you will earn { new_salary*12 - current_salary*12 } per year')