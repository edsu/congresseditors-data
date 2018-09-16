all: diffs users

diffs:
	./diffs.py archive/tweets.csv > diffs.jsonl

users:
	./users.py diffs.jsonl > users.jsonl

