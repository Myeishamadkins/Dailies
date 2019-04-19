# Ask the user for two numbers (x, y)

# Print the times tables up to x * y

# Each line should look like the following example: 

#  2 * 3 = 6

def get_num():
    # num1 = int(input("Give me a number: "))
    # num2 = int(input("Give me another number: "))

    # for num in range(num2 + 1):
    #     total = num * num2
    #     if num > 0:
    #         print(f"{num} * {num2} = {total}")

    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))

    n = 1
    while (n < num2):
        total = n * num2
        print(f"{n} * {num2} = {total}")

        n += 1


def main():
    get_num()


if __name__ == "__main__":
    main()
