touch test.txt
#(place to extract from) >> test.txt
value=$(sed -n 11p test.txt | sed -E 's/.* "detailCSV": (.*)/\1/' | tr -d '"')
python3 extract.py "$value"
python3 partition.py
rm -rf test.csv test.txt 
