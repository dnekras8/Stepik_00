#2022/11/18
def cesar_scramble(text, step_direction, lang):
    alp_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    alp_en = 'abcdefghijklmnopqrstuvwxyz'
    alp = ''
    scr_text = ''
    #start_point = 0
    idx_pos = 0
    if lang.upper() == 'EN':
        alp = alp_en
    elif lang.upper() == 'RU':
        alp = alp_ru
    #if step_direction < 0:
    #    start_point = len(alp)
    alp = alp * 2
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                alp = alp.lower()
            else:
                alp = alp.upper()
            if text[i] in alp:
                idx_pos = alp.index(text[i])
                #scr_text += alp[start_point + step_direction + idx_pos]
                scr_text += alp[(step_direction + idx_pos) % len(alp)]
            else:
                scr_text += text[i]
        else:
            scr_text += text[i]
    return scr_text

def cesar_scramble_x(text, step_direction, lang):
    #step_direction values must be (1; -1)
    sct_text = ''
    x = 0
    sct_text_list = []
    sct_text_list = text.split()
    for i in range(len(sct_text_list)):
        x = sum(1 for l in range(len(sct_text_list[i])) if sct_text_list[i][l].isalpha())
        #print(str(x) , sct_text_list[i])
        if len(sct_text_list[i]) == x and x > 0:
            sct_text += cesar_scramble(sct_text_list[i], x * step_direction, lang)
        else:
            for j in range (len(sct_text_list[i])):
                sct_text += cesar_scramble(sct_text_list[i][j], x * step_direction, lang)
                j += 1
        i += 1
        if i != len(sct_text_list) :
            sct_text += ' '
    return sct_text

# print(cesar_scramble_x('Day, mice. "Year" is a mistake!', 1, 'EN'))
print(cesar_scramble_x('my name is Python!', 1, 'EN'))

# print(cesar_scramble('ТекстТ', 2, 'RU'))
# print(cesar_scramble('ФзмуфФ', -2, 'RU'))
# print(cesar_scramble('English', 20, 'EN'))
# print(cesar_scramble('Yhafcmb', -20, 'EN'))
