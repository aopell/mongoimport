#!/bin/bash

curl -L https://www.fec.gov/files/bulk-downloads/2020/indiv20.zip -o indiv20.zip

unzip indiv20.zip

cd by_date

cd ..
mkdir output

python2 clean.py

FILES=./output/*
for f in $FILES
do
    mongoimport -d=fec -c=zipcode  --type=csv --fieldFile=./header.csv --file=$f
done
