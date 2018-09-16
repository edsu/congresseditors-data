#!/usr/bin/env python

# generate some overview stats from diffs.jsonl and users.jsonl

import gzip
import json

bots = {}
anon = {}
for line in gzip.open('users.jsonl.gz'):
    user = json.loads(line)
    if 'invalid' in user:
        anon[user['name']] = True
    elif 'bot' in user['groups']:
        bots[user['name']] = True

bot_count = 0
anon_count = 0
regular_count = 0
delete_count = 0
for line in gzip.open('diffs.jsonl.gz'):
    diff = json.loads(line)
    if 'touser' not in diff:
        delete_count += 1 
    elif diff['touser'] in bots:
        bot_count += 1
    elif diff['touser'] in anon:
        anon_count += 1
    else:
        regular_count += 1

total = delete_count + bot_count + anon_count + regular_count

print('delete: %s %0.3f' % (delete_count, delete_count / float(total)))
print('bot: %s %0.3f' % (bot_count, bot_count / float(total)))
print('anon: %s %0.3f' % (anon_count, anon_count / float(total)))
print('regular: %s %0.3f' % (regular_count, regular_count / float(total)))


