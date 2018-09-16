#!/usr/bin/env python3

import csv
import json
import time
import requests

from urllib.parse import urlparse, parse_qs

def main():
    for diff in diffs():
        print(json.dumps(diff))
        time.sleep(.5)

def diffs():
    for from_id, to_id, tweet in diff_ids():
        url = 'https://en.wikipedia.org/w/api.php?action=compare&fromrev={}&torev={}&prop=diff|ids|title|diffsize|user|comment|parsedcomment|size&format=json'.format(from_id, to_id)
        diff = requests.get(url).json().get('compare', None)

        # sometimes revisions are deleted in which case nothing is returned
        # from the API in those cases only the revision ids and the tweet are 
        # returned, to at least show that the edit happened. the user 
        # who made the edit and the page that was edited should be available
        # in the text of the tweet

        if diff is None:
            diff = {
                'fromrevid': from_id,
                'torevid': to_id,
            }

        diff['tweet'] = tweet
        yield diff

def diff_ids():
    for tweet in csv.DictReader(open('archive/tweets.csv')):
        uri = urlparse(tweet['expanded_urls'])
        params = parse_qs(uri.query)
        if 'diff' in params:
            yield params['oldid'][0], params['diff'][0], tweet

if __name__ == "__main__":
    main()
