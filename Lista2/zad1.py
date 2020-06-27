import sys

def statistics(filename):
    ''' Returns number of bytes, chars, lines and maximal number of words in line '''
    number_of_bytes = 0
    number_of_words = 0
    number_of_lines = 1
    words_in_line = 1
    bytes_in_line = 0
    max_words_in_line = 0

    with open(filename, encoding='utf-8') as file:
        byte = file.read(1)
        while byte:
            number_of_bytes += 1
            if str(byte) == '\n':
                number_of_lines += 1
                if bytes_in_line > 0:
                    number_of_words += words_in_line
                if max_words_in_line < words_in_line:
                    max_words_in_line = words_in_line
                words_in_line = 1
                bytes_in_line = 0
            elif str(byte) == ' ':
                words_in_line += 1
            elif not str(byte).isspace():
                bytes_in_line += 1
            byte = file.read(1)

        if not number_of_bytes:
            number_of_lines = 0
            number_of_words = 0
        elif bytes_in_line:
            number_of_words += words_in_line
            if max_words_in_line < words_in_line:
                max_words_in_line = words_in_line

    return number_of_bytes, number_of_lines, number_of_words, max_words_in_line   


if __name__== "__main__":
    number_of_bytes, number_of_lines, number_of_words, max_words_in_line = statistics(sys.argv[1])
    print(f'bytes = {number_of_bytes}')
    print(f'line = {number_of_lines}')
    print(f'words = {number_of_words}')
    print(f'max words in line = {max_words_in_line}')
