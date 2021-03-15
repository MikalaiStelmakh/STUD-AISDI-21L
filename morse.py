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

def read_code_reversed(file_path):
    with open(file_path) as f:
        return len(f.readlines())

read_text = read_code_reversed("text.txt")

