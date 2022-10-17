import sys
import os


def main(args):
    print(args)
    print()
    print(os.environ)


if __name__ == "__main__":
    main(sys.argv)