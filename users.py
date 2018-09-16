#!/usr/bin/env python

import json
import requests

def main():
    users = get_users()
    start = 0
    for end in range(0, len(users), 50):
        print_users(users[start:end])
        start = end
    if end < len(users):
        print_users(users[end:len(users)])

def get_users():
    users = set()
    for line in open('diffs.json'):
        diff = json.loads(line)
        # revisions that have been deleted will not have fromuser and touser
        if 'fromuser' in diff:
            users.add(diff['fromuser'])
        if 'touser' in diff:
            users.add(diff['touser'])
    return(list(users))

def print_users(users):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'list': 'users',
        'ususers': '|'.join(users),
        'usprop': 'blockinfo|groups|groupmemberships|implicitgroups|rights|editcount|registration|emailable|gender|centralids|cancreate',
        'format': 'json'
    }
    for user in requests.get(url, params=params).json()['query']['users']:
        print(json.dumps(user))

if __name__ == "__main__":
    main()
