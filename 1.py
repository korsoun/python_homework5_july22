# Удалить из текста слова, содержащие 'абв'

def istheretext (string, part_string):
    thereis = False
    for i in range(len(string)-len(part_string)+1):
        if string[i:i+len(part_string)] == part_string:
            thereis = True
    return thereis

def delete_words (text, part_of_text):
    find = istheretext
    text_list = text.split()
    new_text_list = []
    for word in text_list:
        if not find(word, part_of_text):
            new_text_list.append(word)
    new_text = ''
    for word in new_text_list:
        new_text += f' {word}'
    return new_text

text = 'авог нро ваа абв абвег дштдла пкпк ертабв'
str = 'абв'
print(delete_words(text, str))
