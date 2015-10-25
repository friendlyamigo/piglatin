import sys
import re


def read_file(FILE_ONE):
    with open(FILE_ONE, 'r') as file_one:
        data = file_one.read()
        return split_sentence(data)


def convert_file(FILE_ONE):
    word_array = []
    for word in FILE_ONE:
        word = convert_word(word)
        word_array.append(word)
    return "".join(word_array)


def write_file(CONVERTED_FILE, OUTPUT_FILE):
    with open(OUTPUT_FILE, 'w') as output_file:
        output_file.write(CONVERTED_FILE)


# find vowel position, helper functionto convert word
def find_vowel_position(WORD):
    for letter in WORD:
        if letter in vowels:
            return WORD.index(letter)


# convert individual words
def convert_word(WORD):
    if WORD[0] in vowels:
        return WORD.lower() + 'yay'
    elif WORD[0].isalpha():
        vowel_pos = find_vowel_position(WORD)
        return WORD[vowel_pos:].lower() + WORD[:vowel_pos].lower() + 'ay'
    else:
        return WORD


# split a sentence by whitespace and punctuation
def split_sentence(SENTENCE):
    return re.findall(r"[\w']+|[\"\'.,!?; \n]", SENTENCE)


vowels = ['a', 'e', 'i', 'o', 'u']
input_file = read_file(sys.argv[1])
converted_file = convert_file(input_file)
write_file(converted_file, sys.argv[2])
