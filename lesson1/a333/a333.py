# Make a more advanced storage converter. Write a program that receives a amount of storage from a user,
# including its units, and converts the amount to the highest possible unit such that the whole part of the number will be higher than 0.
# Round the result to the first digit after the decimal point.
# For example, if the user enters: 1000000 bytes, you should print: "967.6 kb". For the input 1200000 bytes, print: "1.1 mb"


number = int(input("Please enter the number of the storage amount: "))
from_unit = input("Please enter the unit of the storage to convert from (bytes/kb/mb/gb/tb): ")

tb_mult = 1024**4
gb_mult = 1024**3
mb_mult = 1024**2
kb_mult = 1024

in_bytes = 0;

if from_unit == 'tb':
    in_bytes = number * tb_mult
if from_unit == 'gb':
    in_bytes = number * gb_mult
if from_unit == 'mb':
    in_bytes = number * mb_mult
if from_unit == 'kb':
    in_bytes = number * kb_mult
if from_unit == "bytes":
    in_bytes = number

if in_bytes / tb_mult >= 1:
    print(round(in_bytes / tb_mult, 1), 'tb')
elif in_bytes / gb_mult >= 1:
    print(round(in_bytes / gb_mult, 1), 'gb')
elif in_bytes / mb_mult >= 1:
    print(round(in_bytes / mb_mult, 1), 'mb')
elif in_bytes / kb_mult >= 1:
    print(round(in_bytes / kb_mult, 1), 'kb')
else:
    print(in_bytes, 'bytes')