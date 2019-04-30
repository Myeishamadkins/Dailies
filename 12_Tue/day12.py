def infinite_repetition(letter, length):
    count_letter = letter.count("a")
    string_length = max(1, len(letter[:length]))
    result = count_letter // string_length
    return(result)


if __name__ == "__main__":
    print(infinite_repetition('a', 50), 'should be', 50)
    print(infinite_repetition('ab', 60), 'should be', 30)
    print(infinite_repetition('aba', 5), 'should be', 3)
    print(infinite_repetition('c', 1000), 'should be', 0)
    print(infinite_repetition('A', 100), 'should be', 0)
    print(infinite_repetition('', 1), 'should be', 0)
    print(infinite_repetition('a', 0), 'should be', 0)
    print(infinite_repetition('ab', 1), 'should be', 1)
