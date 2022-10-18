import sys
import os
import json


def get_github_action_event():
    with open(os.environ["GITHUB_EVENT_PATH"]) as f:
        data = json.load(f)
        return data

def get_shortcut_access_token():
    return os.environ["SHORTCUT_ACCESS_TOKEN"]


def main(args):
    print(args)
    print()
    print(get_github_action_event())
    print()
    print(get_shortcut_access_token())


if __name__ == "__main__":
    main(sys.argv)