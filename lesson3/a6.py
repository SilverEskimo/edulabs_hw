# Self-learning exercise. There is a new feature called structural pattern matching that has been introduced in Python3.10.
# Read about match-case statements in python documentation or in any other source and implement the following exercise using this feature.
#
# Write a simple program that receives a country and displays the currency of that country according to the following:
# USA -> US dollar
# Israel - New Israel Shequel (NIS)
# UK -> Pound
# All the EU countries (Germany, Austria, Czech, France, Italy, Spain,...) -> Euro
# If user provides any other country, print “I don’t know”

eu_countries = ["austria", "belgium", "cyprus", "estonia", "finland", "france", "germany", "greece", "ireland",
                "italy", "latvia", "lithuania", "luxembourg", "malta", "netherlands", "portugal", "slovakia",
                "slovenia", "spain", "holland"]
country = input("Please enter a country: ").strip().lower()

match country:
    case "israel":
        print("New Israeli Shekel")
    case country if country == "usa" or country == "united states" or country == "america" or country == "us":
        print("US Dollar")
    case country if country == "uk" or country == "united kingdom" or country == "england":
        print("Pound")
    case country if country in eu_countries:
        print("Euro")
    case _:
        print("I don't know")

