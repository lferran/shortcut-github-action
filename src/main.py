import sys
import os
import json


def get_github_action_event():
    with open(os.environ["GITHUB_EVENT_PATH"]) as f:
        data = json.load(f)
        return data


def main(args):
    print(args)
    print()
    print(os.environ)
    print()
    print(get_github_action_event())


if __name__ == "__main__":
    main(sys.argv)