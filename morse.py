MORSE_CODE_reversed = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                    }


def encryption(lines):
    text = []
    for line in lines:
        new_word = []
        line = line.split()
        for word in line:
            for character in word:
                if character.upper() in MORSE_CODE_reversed:
                    new_word.append(MORSE_CODE_reversed[character.upper()] + ' ')
            if new_word[-1] != '/ ':
                new_word.append('/ ')
        text.append(' '.join(new_word[:-1]))
    return '\n'.join(text)


def read_code_reversed(file_path):
    with open(file_path) as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    read_text = read_code_reversed("text.txt")
    print(encryption(read_text))
