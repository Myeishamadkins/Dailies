# Ask the user to provide a positive integer (x)
# For each number (n) less than x, print whether or not the number is even or odd.

num = int(input("Enter a number: "))

# for n in range(num):
#     if n != 0:
#         if n % 2:
#             print(f'{n} : odd')
#         else:
#             print(f'{n} : even')

i = 1
while (i < num):
    if i != 0:
        if i % 2 == 0:
            print(f" {i} : Even")

        else:
            print(f" {i} : Odd")
    i += 1
