x = 1
while x < 10:
    if x == 4:
        # Next line helps us incrementing regardless of the continue
        x += 1
        # Next statement skips the lines below and reruns to the beginning of the loops
        continue
    print(x)
    x += 1
