age = int(input('Please submit your age: '))
if age <= 14:
    print('Sorry, you must be over 14.')
elif age < 18:
    print('Users under the age of 18 must have perimission from a parent.')
else:
    print('Welcome aboard')

