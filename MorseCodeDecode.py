import random

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

text = input('Enter your text: ')
cipher = ''
for s, v in enumerate(text):
    if v != ' ':
        if s != len(text) - 1 and text[s+1] != ' ':
            cipher += MORSE_CODE_DICT[v.upper()] + ' '
        else:
            cipher += MORSE_CODE_DICT[v.upper()]
    else:
        cipher += '  '
cipher += '   '

cipher_cycle_slise = (cipher * 20)[random.randint(1, len(cipher)):]
cipher_cycle_slise_reversed = cipher_cycle_slise[::-1]

print(f'Basic Coding result is: [{cipher}]')
print(f'Cycled and shifted code is: {cipher_cycle_slise}')

pattern = 'not found'
i = 1
slice_check = False
while not slice_check:
    slices_list = [cipher_cycle_slise_reversed[l:l + i] for l in range(0, len(cipher_cycle_slise_reversed), i)]
    slice_check = True
    for index, value in enumerate(slices_list):
        if index != len(slices_list) - 1:
            if slices_list[0] != slices_list[index]:
                slice_check = False
                break
    if slice_check:
        pattern = slices_list[0]
        break
    else:
        i += 1

print(f'Defined pattern is: [{pattern[::-1][:len(pattern)-3].replace("  ", " _ ")}]')
cipher_prepared = pattern[::-1][:len(pattern)-3].replace('  ', ' _ ').split()

decipher = ''
for t in cipher_prepared:
    if t == '_':
        decipher += ' '
    else:
        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(t)]

print(f'Final decoding is: [{decipher}]')
