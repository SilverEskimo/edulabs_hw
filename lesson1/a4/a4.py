scifi_books = int(input("Please enter the amount of sci-fi books: "))
comics_books = int(input("Please enter the amount of comics books: "))
history_books = int(input("Please enter the amount of history books: "))

scifi_price = 58
comics_price = 32
history_price = 24

before_discount = scifi_price*scifi_books + history_price*history_books + comics_price*comics_books
total_discount = 0

if scifi_books >= 3:
    total_discount += scifi_books*scifi_price*0.1
if history_books >= 3:
    total_discount += (history_books//3)*history_price
if before_discount >= 300:
    total_discount += 20

total_price = before_discount - total_discount
print(f'Total before discount: {before_discount} \nTotal discount: {total_discount} \nTotal to pay: {total_price}')

