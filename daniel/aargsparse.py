import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog="Daniel Program",
        description="Enter a num and get num*4",
    )

    parser.add_argument('number', help="Number to insert")
    parser.add_argument('-o', '--options', help="Your options")
    parser.add_argument('-n', '--name', help="Please enter your name")

    args = parser.parse_args()
    print(args)

    print(int(args.number) * 4)
    print(args.options)
