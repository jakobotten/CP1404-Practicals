lower = 48
upper = 123
print("Enter a number ({}-{}):".format(lower, upper))
for i in range(lower, upper, 1):
    print("{:>4} {:>4}".format(i, chr(i)))