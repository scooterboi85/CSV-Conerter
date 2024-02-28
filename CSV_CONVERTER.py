
#list every csv file in the currect directory 
#for the rows with timestamps 0.1-0.2
#write row[1] of the input to row[i] of the output 
import csv
import os


def extractor(filename, table):
  in_file = open(filename)
  #Each row returned by the reader is a list of String  
  #elements containing the data found by removing the delimiters
  csv_reader = csv.reader(in_file, delimiter=',')
  n = 0
  for row in csv_reader:
    if len(row) > 1 and float(row[0]) >= 0.1 and float(row[0]) <= 0.2:
      table[n].append(row[1])
      n += 1
    if n == 21: 
      break   
  in_file.close()


#get names of all files in directory 
filenames = []
for x in os.listdir(os.getcwd()):
    if x.endswith(".csv") and x != "OUTPUT.csv":
      filenames.append(x)

table = []
i = 0.1
while i <= 0.2:
  table.append([str(i)])
  i += 0.005
  i = round(i, 3)


for file in filenames:
 extractor(file, table)

row_list = []
for row in table:
  row_list.append(', '.join(row))

f = open("OUTPUT.csv", 'w')
titles = "time, " + ", ".join(filenames) + '\n'
f.write(titles)
for row in row_list:
  f.write(row+'\n')
f.close()
print("Output written to file \'OUTPUT.txt\'.")
