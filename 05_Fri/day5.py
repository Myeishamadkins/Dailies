# Ask the user for a string (_s_)
# Print a "bar chart" for the string where each line is the characters distance from "a" plus 1. 
# If the character is not alphabetical, simply print it on a line by itself.
# For example "Base Camp Coding Academy" would print:

# B
# a
# sssssssssssssssssss
# eeeee

# CCC
# a
# mmmmmmmmmmmmm
# pppppppppppppppp
# CCC
# ooooooooooooooo
# dddd
# iiiiiiiii
# nnnnnnnnnnnnnn
# ggggggg

# A
# ccc
# a
# dddd
# eeeee
# mmmmmmmmmmmmm
# yyyyyyyyyyyyyyyyyyyyyyyyy

def get_string():
    string = input("Give me a string: ")
    return string


def logic(string):
    for ch in string:
        length = (ord(ch.lower()) - 97) + 1
        if (length > 0 and length <= 26):
            print(ch * length)
        else:
            print(ch)


def main():
    string = get_string()
    logic(string)


if __name__ == '__main__':
    main()
