age = int(input('Enter your age: '))
location = input('Enter your country: ')

if (age >= 17 and location =='UK') or (age >= 16 and location == 'Canada'):
    print('You can learn to drive')
else:
    print(f"You cannot learn how to drive. You're {age}")

