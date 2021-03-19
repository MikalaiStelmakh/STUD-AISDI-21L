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


def encryption(lines: list) -> str:
    text = []
    for line in lines:
        new_word = []
        for index, word in enumerate(line):
            for char in word:
                if char.upper() in MORSE_CODE_reversed:
                    if not (char == ' ' and new_word[-1] == '/ '):
                        isLastWord = True if index == len(line) - 1 else False
                        space = ' ' if not isLastWord else ''
                        new_word.append(MORSE_CODE_reversed[char.upper()] + space)
        text.append(' '.join(new_word))
    return '\n'.join(text)


def read_from_file(file_path) -> list:
    with open(file_path) as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    lines = read_from_file(args.file)
    print(encryption(lines))
