# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import os
os.system("cls")

with open('task041_RLE1_decoded.txt', 'r') as data:
    my_text = data.read()


def encode_rle(ss):  # кодировка
    str_code = ''
    count = 1       # счетчик количества  символов
    for i in range(len(ss)):
        if i < len(ss)-1:
            if ss[i] == ss[i + 1]:
                count += 1
            else:
                a = ss[i]
                str_code += str(count) + ss[i]
                count = 1
        else:
            str_code += str(count) + ss[i]
    return str_code


# кодировка
str_code = encode_rle(my_text)
print('Исходник: ', my_text)
print('Обработанный: ', str_code, '\n')

with open('task041_RLE2_encoded.txt', 'r') as data:
    my_text2 = data.read()

# декодировка


def decoding_rle(ss):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print('Исходник: ', my_text2)
print('Обработанный: ', str_decode, '\n')