# Write a program that receives the length of the movie in minutes,
# and prints out the length of the movie in the following format: hh:mm.
# For example, if the input is 135, your program should print: 2:15

time_in_mins = int(input("Please enter the movie length in minutes: "))
print(f'The length in hh:mm format is: { int(time_in_mins / 60) }:{ time_in_mins  % 60 }')