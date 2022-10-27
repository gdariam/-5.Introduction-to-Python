# Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
from unittest import result
def clear(): return os.system('cls')


clear()

def compress_rle(text):
    result = ''
    pred_symbol = ''
    index = 1
    for char in text:
        if char != pred_symbol:
            if pred_symbol:
                result += str(index) + pred_symbol
            index = 1
            pred_symbol = char
        else:
            index += 1
    else:
        result += str(index) + pred_symbol
    return result

def decompress_text(text):
    result = ''
    index = ''
    for char in text:
        if char.isdigit():
            index += char
        else:
            result += char * int(index)
            index = ''
    return result

with open('not_compress.txt', 'r') as file:
    not_compress = file.readline()

result_compress = compress_rle(not_compress)

with open ('compress.txt', 'r') as file:
    compress = file.readline()
result_decompress = decompress_text(compress)

with open('decompress.txt', 'w') as file:
    file.write(f'{result_decompress}')