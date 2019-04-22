# Using a single loop, compute the difference between the
# largest value and smallest value in a given list
# ```python

# [10, 0, 20, 10] # answer is 20
# [5, 5] # answer is 0
# [13] # answer is 0
# [20, 10, 0, 10] # answer is 20
# [1, 2, 3, 4, 5] # anwser is 4

def prac():

    lst = []
    num = int(input('How many numbers: '))

    for n in range(num):

        numbers = int(input('Enter number '))

        lst.append(numbers)

    snum = lst[0]

    bnum = lst[0]

    for num in lst:

        if num < snum:

            snum = num

        elif num > bnum:

            bnum = num

    print('The answer is {}'.format(bnum - snum))






