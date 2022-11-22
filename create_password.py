#2022/11/17
from random import choice, shuffle

def is_yes_reply(text):
    rep = input(text).lower()
    while rep not in ('y', 'n'):
        rep = input(text).lower()
    return rep == 'y'

def str_exclude(textmain, textexcl):
    res = textmain
    for l in textexcl:
        res = res.replace(l,'')
    return res

def charstring_prep():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    exclution = 'il1Lo0O'
    temp_txt = ''
    charsl = []
    charsg = []
    if is_yes_reply('Включать ли цифры 0123456789? (y/n)'):
        charsl.append(digits)
    if is_yes_reply('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)'):
        charsl.append(uppercase_letters)
    if is_yes_reply('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)'):
        charsl.append(lowercase_letters)
    if is_yes_reply('Включать ли символы !#$%&*+-=?@^_? (y/n)'):
        charsl.append(punctuation)
    if is_yes_reply('Исключать ли неоднозначные символы il1Lo0O? (y/n)') and len(charsl)>0:
        for i in range(len(charsl)):
            charsl[i] = str_exclude(charsl[i], exclution)
            #charsg[i] = len(charsl[i])
            charsg.append(len(charsl[i]))
    return charsl, charsg

def get_pass(list_chars, list_ch_qty, chars_qty):
    temp_text = ''
    i = 0
    temp_list = ''
    while i <= chars_qty and chars_qty>=len(list_ch_qty):
        for j in range(len(list_ch_qty)):
            if i == 0 or i <= chars_qty: # minimum 1 char from every group
                temp_text = temp_text + choice(list_chars[j])
                i += 1
    #temp_text = shuffle(*list(temp_text)) #has to be list()
    temp_list = list(temp_text)
    shuffle(temp_list)
    temp_text = ''.join(temp_list)
    return temp_text

def create_passwords():
    l1, n1 = [], []
    cntPw = int(input('Укажите количество паролей для генерации:'))
    lenPw = int(input('Укажите длину одного пароля:'))
    l1, n1 = charstring_prep()
    # print(l1)
    while cntPw > 0:
        print(get_pass(l1, n1, lenPw))
        cntPw -= 1
#------------------------
create_passwords()

#print(get_input_int())
#print(is_yes_reply('Durak?'))

# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# exclution = 'il1Lo0O'
# n = 0
#

