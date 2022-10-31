import random
MORSE_CODE_DICT = {'A': '.-',       'B': '-...',
                   'C': '-.-.',     'D': '-..',     'E': '.',
                   'F': '..-.',     'G': '--.',     'H': '....',
                   'I': '..',       'J': '.---',    'K': '-.-',
                   'L': '.-..',     'M': '--',      'N': '-.',
                   'O': '---',      'P': '.--.',    'Q': '--.-',
                   'R': '.-.',      'S': '...',     'T': '-',
                   'U': '..-',      'V': '...-',    'W': '.--',
                   'X': '-..-',     'Y': '-.--',    'Z': '--..'}

text = input('Enter your text: ')
cipher = ''
for _ in text:
    if _ != ' ':
        cipher += MORSE_CODE_DICT[_.upper()] + ' '
    else:
        cipher += ' '

cipher_cycle_slise = (cipher * 20)[random.randint(1, len(cipher)):]
cipher_cycle_slise_reversed = cipher_cycle_slise[::-1]

print(cipher_cycle_slise)
print(cipher)

pattern = 'not found'
i = 1
slice_check = False
while not slice_check:
    slices_list = [cipher_cycle_slise_reversed[_:_ + i] for _ in range(0, len(cipher_cycle_slise_reversed), i)]
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

print(pattern[::-1])
print(pattern[::-1].split())
print(pattern[::-1].replace('  ', ' space ').split())

cipher_prepared = pattern[::-1].replace('  ', ' space ').split()

decipher = ''
for _ in cipher_prepared:
    if _ == 'space':
        decipher += ' '
    else:
        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(_)]

print(decipher.capitalize())
