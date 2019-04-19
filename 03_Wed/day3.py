# Ask the user to provide two strings (s1, s2)

# Print a new string where each character is either:

#  - "." if the strings had different characters in that position

#  - the character that was shared in that position

# This means "hello" and "pillow" would print "..llo."


def get_string():
    string = input("Insert String: ")
    return string


def getString(string_one, string_two):
    string_one = []
    string_two = []
    i = 0
    sameLetter = ""
    for s in string_one:
        string_one.append(s)
    for s in string_two:
        string_two.append(s)

    while (i < len(string_one) and i < len(string_two)):
        if (string_one[i] != string_two[i]):
            sameLetter += "."
        else:
            sameLetter += string_one[i]
        i += 1

    return sameLetter


def main():
    string_one = get_string()
    string_two = get_string()
    print(getString(string_one, string_two))


if __name__ == '__main__':
    main()
