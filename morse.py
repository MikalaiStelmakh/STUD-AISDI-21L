import argparse


MORSE_CODE_reversed = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
    }


def encryption(lines):
    text = []
    for line in lines:
        new_word = []
        for word in line:
            for char in word:
                if char.upper() in MORSE_CODE_reversed:
                    if not (char == ' ' and new_word[-1] == '/ '):
                        new_word.append(MORSE_CODE_reversed[char.upper()] + ' ')
        text.append(' '.join(new_word))
    return '\n'.join(text)


def read_code_reversed(file_path):
    with open(file_path) as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    read_text = read_code_reversed(args.file)
    print(encryption(read_text))
