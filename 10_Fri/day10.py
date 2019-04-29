# ransom note
def prac():
    magazine = 'Hello World'
    note = 'He old'

    mag = list(magazine)
    n = list(note)

    for letters in n:
        if letters in mag and letters != " ":
            mag.remove(letters)
        elif letters == " ":
            continue
        else:
            return False
    return True

def run_fun():
    print(prac())

if __name__ == "__main__":
    run_fun()
