import csv

# We want to create a set so we have a unique list of students
valid_drivers = set()
with open('output/drivers.csv') as csv_file:
    reader = csv.reader(csv_file)
    # Next function allows us to skip over to the next item 
    # when we're iterating through a list of items.
    next(reader)
    for line in reader:
        passed_theory = line[2]
        passed_practical = line[3]
        if passed_theory == 'True' and passed_practical == 'True':
            valid_drivers.add(line[0])

print(valid_drivers)
