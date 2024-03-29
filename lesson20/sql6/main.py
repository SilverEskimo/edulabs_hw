from my_parser import MyParser
from db_connection import DBConnector


if __name__ == '__main__':
    parser = MyParser()
    db = DBConnector()
    args = parser.args

    if args.name:
        r = db.check_if_movie_in_db(args.name)
        if r:
            print(f"Release date: {r[0]}\nRating: {r[1]}")
        else:
            print("The movie does not exist")
    elif args.rating:
        res = db.return_with_min_rating(args.rating)
        if not res:
            print(f"There are no movies with rating above {args.rating}")
        else:
            print(f"Movies with rating above {args.rating}: ")
            for r in res:
                print(f"Name: {r[0].title()}, Rating: {r[1]}")
    else:
        print("Nothing to do, bye bye")
        exit(0)


