import csv
from os import listdir
from os.path import isfile, join
import os

mypath = os.getcwd()  + "/by_date"
output_path =  os.getcwd() + "/output/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)
for file_name in onlyfiles:
    csv_file = output_path + file_name[:len(file_name) -4] + ".csv"
    in_txt = csv.reader(open(mypath + "/" + file_name, "rb"), delimiter = '|')
    out_csv = csv.writer(open(csv_file, 'wb'))

    out_csv.writerows(in_txt)
    print("Converted " + csv_file)
