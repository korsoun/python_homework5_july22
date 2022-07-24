# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coder(text):
    coded_text = ''
    # Индекс для перебора элементов.
    position = 1
    # Позиция начала последовательности.
    row_start_pos = 0
    repeats = 1
    # Перебор элементов
    while position != len(text)-1:
        # Если текущий элемент входит в последовательность, копятся данные для шифра.
        if text[position] == text[row_start_pos]:
            repeats += 1
            # Если при этом следующий элемент начинает другую последовательность, происходит запись шифра текущей последовательности.
            if text[position + 1] != text[row_start_pos]:
                coded_text += f'{repeats}{text[row_start_pos]}'
                repeats = 0
                row_start_pos = position + 1
        # Если последний элемент продолжает последовательность, он считается в количестве повторов заранее, и происходит запись шифра и закрытие цикла.
        if text[len(text)-1] == text[row_start_pos] and position == len(text)-2:
            repeats += 1
            coded_text += f'{repeats}{text[row_start_pos]}'
        position += 1
    return coded_text
         
def decoder (text):
    encoding_str = ''
    # Списки, хранящие количество повторений и соответствующие им символы.
    repeats_list = []
    symbols_list = []
    position = 0
    repeats_qnt = ''
    while position != len(text):
        # Если текущий элемент число, он записывается в строку repeats.
        if text[position].isdigit():
            repeats_qnt += text[position]
            # При этом, если следующий элемент не число, repeats записывается в список, и строка repeats обнуляется для нового набора числа.
            if not text[position+1].isdigit():
                repeats_list.append(int(repeats_qnt))
                repeats_qnt = ''
        # Если текущий элемент не число, он записывается в список символов.
        if not text[position].isdigit():
            symbols_list.append(text[position])
        position += 1
    # Составляется расшифрованная строка повторением символов нужное количество раз.
    for i in range(len(repeats_list)):
        encoding_str += symbols_list[i] * repeats_list[i]
    return encoding_str

# 'text_for_coding.txt' - изначальный файл. Записанная в нем строка шифруется и передается в создаваемый файл 'coded_text.txt'.
# Из 'coded_text.txt' зашифрованная строка дешифруется и записывается в создаваемый файл 'decoded_text.txt'.
text_for_coding = ''
with open('text_for_coding.txt', 'r') as code_file:
    text_for_coding = code_file.readline()


coded_text = coder(text_for_coding)
with open('coded_text.txt', 'w') as code_file:
    code_file.writelines(coded_text)

text_for_decoding = ''
with open('coded_text.txt', 'r') as decode_file:
    text_for_decoding = decode_file.readline()
decoded_text = decoder(text_for_decoding)

with open('decoded_text.txt', 'w') as decode_file:
    decode_file.writelines(decoded_text)

# Если изначальная строка будучи закодированной, а затем раскодированной, равна сама себе, то задание выполнено.
if coded_text == coder(decoded_text):
    print('Задание выполнено')
