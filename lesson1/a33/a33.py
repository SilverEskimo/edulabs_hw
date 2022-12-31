# Write a simple storage converter - a program that converts an amount of bytes between byte units.
# Your program should get from a user a number that represents storage amount,
# a unit of the amount provided (bytes, kb, mb, gb, tb), and a unit the user wants to convert the storage to.
# The program should convert the amount to the desired unit.
# For example, if the user asks to convert 2048 bytes to kb, your program should return: 2 kb.
# If the user tries to convert 128 mb to gb, the expected result is: 0.125 gb

number = int(input("Please enter the number of the storage amount: "))
from_unit = input("Please enter the unit of the storage to convert from (bytes/kb/mb/gb/tb): ")
to_unit = input("Please enter the desired unit to convert to (bytes/kb/mb/gb/tb): ")

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

if to_unit == 'bytes':
    print(in_bytes, "bytes")
elif to_unit == 'kb':
    print(in_bytes/kb_mult, "kb")
elif to_unit == 'mb':
    print(in_bytes/mb_mult, "mb")
elif to_unit == 'gb':
    print(in_bytes/gb_mult, "gb")
elif to_unit == 'tb':
    print(in_bytes/tb_mult, "tb")