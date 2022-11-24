from random import choice

WORD_LIST=['кукуруза', 'бревно', 'дом']

def get_word():
    return choice(WORD_LIST).upper()

def display_hangman(tries):
    #Для вывода символа бэкслеша \ используется экранирование символа с помощью \, то есть комбинация \\
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries>0:
        is_new_input_ok = False
        #check_new_input
        while not is_new_input_ok:
            s = input('Введите букву или слово целиком: ').lower()
            if len(s) == 1:
                if s in guessed_letters:
                    print('Вы уже вводили букву: ' + s)
                else:
                    guessed_letters.append(s)
                    is_new_input_ok = True
            if len(s) > 1:
                if s in guessed_words:
                    print('Вы уже вводили слово: ' + s)
                else:
                    is_new_input_ok = True
                guessed_words.append(s)
        for i in range(len(word)):
            if str(word[i]).lower() == s:
                word_completion = word_completion[:i] + s + word_completion[(i+1):]
                #print(word_completion)
        # if len(s) > 1: #remember tried word & letters
        #     guessed_words.append(s)
        # elif len(s) == 1:
        #     guessed_letters.append(s)
        guessed = (word.lower() == s) or (word.lower() == word_completion)
        if guessed:
            break
        if s in word.lower():
            print(word_completion)
        else:
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)
        if not guessed and tries == 0:
            break
    # else:
    #     print('You win ELSE!!!')
    if guessed:
        print('You win!!!')
    else:
        print('You''re done :-(')
    print(word)


play(get_word())
#print(get_word())
#print(display_hangman(6))