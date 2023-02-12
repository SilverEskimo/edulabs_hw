# Q1 - Given a word, check whether it's a Capitalized word (starts from upper case, the second char is a lower case)
# Q2 - Given a string that represents DNA, check whether a given DNA string contain a TATA-box-like pattern:
#      TATA-box-like pattern has the following structure: “TATAA” followed by 3 nucleotides and ends with “TT”
#      Nucleotide is one of: A, C, G, T
#      Example of strings that contain TATA-box-like DNA: "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
#      Example of strings that does not contain TATA-box-like DNA:
#      "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
import re
import string

if __name__ == '__main__':
    # Q1:
    print(re.match("[A-Z][a-z]+", "Aaasdasdas_asd21333"))

    # Q2:
    print(re.search("TATAA[ACGT]{3}TT", "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))

    # Q3: Match two digits then any character then two non digits
    print(re.search("[0-9]{2}.[^0-9]{2}", "Aaasdasd22as_asd21333"))

    # Q4: Check whether the given string contains at least two TATA-like patterns
    print(re.search("(TATAA[ACGT]{3}TT).*(TATAA[ACGT]{3}TT)", "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAATATAAGGGTT"))

    # Q5: Maximum 2 TATA-like patterns

    # Q6: Write a regular expression to look for 3 digits, possibly separated by whitespace.
    print(re.search("([0-9].*){3}", "Aaasdasdas_asd2_1_3"))

    # Q7: Find all the israeli cell phone numbers in the text.
    # In this exercise, israeli cell phone number answers the following:
    # format: <000-0000000>
    # starts from 05
    print(re.search("[0-9]{3}-[0-9]{7}", "asdqwe052-8381023qsqwe"))

    # Q8: Write a function that checks whether the provided string is a valid seat number in an aircraft.
    # The function receives as parameters number of rows in the aircraft, number of seats in a row, and ticket string.
    # For example, if the functions receives as parameters:
    # 52 rows
    # 6 seats in a row -> Chars A - F
    # The valid ticket string will be for example: 32B, 2A, 15F
    # Invalid ticket string: 53A, 23G, 1E
    
    class InvalidTicket(Exception):
        def __init__(self):
            super().__init__("Invalid ticket")

    def check_valid_seat(rows: int, seats: int, ticket: str):
        seats_str = ""
        for num in range(seats):
            seats_str += string.ascii_uppercase[num]
        seat_char = ticket[-1]
        seat_line = ticket[-1:]
        if not re.search(seat_char, seats_str):
            raise InvalidTicket()
        if len(seat_line) == 1:
            if re.search(r"\d" + '[' + seats_str + ']', ticket):
                print("[" + "1" + "-" + str(rows) + "]"+"[" + seats_str + "]" )
                return "Valid"
        # if len(seat_line) == 2:

    print(check_valid_seat(9, 6, "2A"))

