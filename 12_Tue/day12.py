def infinite_repetition(letter, length):
    count_letter = letter.count("a")
    if len(letter) > 0 and letter.count("a") > 0:
        remainder = length % len(letter)
        string_length = letter[:remainder].count("a")
        string = len(letter)   
        result = (length // string) * (count_letter) + (string_length)
    else:
        result = 0
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
    print(infinite_repetition('ab', 5), 'should be', 3)
    
