age = int(input('Enter your age: '))
pass_situation = input("Did you pass your exam?: ")

if (pass_situation == "y" or pass_situation == "Y"):
    pass_flg = True
else:
    pass_flg = False

if age >= 17:
    if pass_flg is True:
        print("You are allowed to drive")
    else:
        print("You can learn to drive")
else:
    print("You are not old enough to drive")
