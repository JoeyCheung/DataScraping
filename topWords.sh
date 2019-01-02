#!/usr/bin/env bash

NUM_WORDS="$1"

curl -s #insert link to extract here |
tr '[:upper:]' '[:lower:]'|
grep -oE '\w+'|
sort |
uniq -c |
sort -nr |
head -n $NUM_WORDS
