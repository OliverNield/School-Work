import csv
dictionary = {}
filein = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/School Work/Things used for code/Monsters.csv','r')
reader = csv.reader(filein)
reader.__next__()
for row in reader:
    id = row[0]
    name = row[1]
    dictionary[id] = name
userin = input('please input the id of the beast you wish to look up')
print(dictionary[userin])