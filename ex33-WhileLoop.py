def myrange(start, end, step=1):
    i = start
    numbers = []
    while i < end:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    return numbers

print("The numbers: ")
for num in myrange(0, 6, 2):
    print(num)