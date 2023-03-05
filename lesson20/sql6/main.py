from my_parser import MyParser
from db_connection import DBConnector


if __name__ == '__main__':
    parser = MyParser()
    db = DBConnector()
    args = parser.args

    if args.name:
        res = db.check_if_movie_in_db(args.name)
        if not res:
            print("The movie does not exist")
            exit(0)
        print(f"Release date: {res[0]}\nRating: {res[1]}")
        exit(0)
    if args.rating:
        res = db.return_with_min_rating(args.rating)
        if not res:
            print(f"There are no movies with rating above {args.rating}")
            exit(0)
        print(f"Movies with rating above {args.rating}: ")
        for r in res:
            print(r.title())
        exit(0)
    else:
        print("Nothing to do, bye bye")
        exit(0)


