#!/bin/bash

#touch html.csv
#touch clean.csv

curl $1  --output sbid.xml

python scrape.py

counter=0
input="sbid.csv"
while IFS= read -r line
do
  python extract.py "$line" "$counter"
  counter=$((counter+1))
done < "$input"

new_counter=0

for file in *.json
do
  touch html$((new_counter)).csv
  json2csv -i test$((new_counter)).json -f html,id >> html$((new_counter)).csv 
  new_counter=$((new_counter+1))
done

rm -rf *.json sbid.csv

python combine.py

mv combined.csv results

rm -rf *.csv sbid.xml

#new_input="html.csv"
#while IFS= read -r line
#do
#  python clean.py "$line"
#done < "$new_input"

#rm -rf html.csv
