all: diffs users

diffs:
	./diffs.py archive/tweets.csv | gzip > diffs.jsonl.gz

users:
	./users.py diffs.jsonl | gzip > users.jsonl.gz

