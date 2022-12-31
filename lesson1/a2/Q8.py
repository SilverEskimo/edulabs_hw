#Bob decided that he is going to donate 14% of his monthly salary to charity.
#Write a program that receives Bob's salary and prints how much he should pass to the charity.

salary = int(input("Bob, please enter your monthly salary: "))
print(f"You should pass {round(salary*0.14,2)} to charity this month")
