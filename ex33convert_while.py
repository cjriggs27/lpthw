# study drill 1 to convert while-loop to function you can call
def study_drill1(n):
    i = 0
    numbers_drill1 = []
    while i < n:
        print(f"Item: {i}")
        numbers_drill1.append(i)

        i = i + 1
    print(numbers_drill1)


# study drill 2 use function to rewrite the scripts to try different numbers
print("\nUsing study_drill1 with n = 3")
study_drill1(3)

print("\nUsing study_drill1 with n = 8")
study_drill1(10)


# study drill 3 add another variable to the function arguments that you can pass in that lets you change the +1 to i to change how much it increments by
def study_drill3(n, s):
    i = 0
    numbers_drill3 = []
    while i < n:
        print(f"Item: {i}")
        numbers_drill3.append(i)

        i = i + s
    print(numbers_drill3)

# study drill 4 use new function variable to change increments
print("\nUsing study_drill3 with n = 20 and s = 2")
study_drill3(20, 2)


# study drill 5 write function to use for-loop and range
print("\nstudy_drill5 will use a for-loop and range")
def study_drill5(n, s):
# these three numbers in range mean (start, stop, step)
    numbers_drill5 = range(0, n, s)

    for i in numbers_drill5:
        print(f"Item: {i}")

    print(numbers_drill5)
study_drill5(40, 4)
