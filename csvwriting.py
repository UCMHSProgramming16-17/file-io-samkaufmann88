# import csv
import csv

# open file in write mode
csvfile = open('randomname.py', 'w')

# create csv writer
csvwriter = csv.writer(csvfile, delimiter=',')

# write to file
csvwriter.writerow(['a', 'b', 'hypotenuse'])


for a in range (1, 11):
    # for each value of a
    csvwriter.writerow([a])

for b in range(1, 11):
    csvwriter.writerow([a, b])

# close file
csvfile.close()
