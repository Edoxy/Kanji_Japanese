import time
import random
import codecs
from os import system, name

from os import fdopen
import string

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


f = codecs.open('kanjilist.txt', 'r', 'UTF-8')
content = f.read()
f.close()

# print(content)
test_list = content.split('\n')
new_list = []
# print(test_list)
for x in test_list:
    t = x.split()
    new_list.append((t[0], t[1]))

lista_errori = []
score = 0
start = time.time()
n_quiz = 6
for i in range(n_quiz):
    clear()
    #formulazione delle opzioni e della domanda
    num = ['a', 'b', 'c', 'd']
    random_option = []
    stringa_quiz = []
    for i in range(0, 4):
        number = random.choice(num)
        kanji = random.choice(new_list)
        num.remove(number)
        new_list.remove(kanji)
        random_option.append((number, kanji))
        stringa_quiz.append(str(number) + ') '+ str(kanji[0]))
    #ordinamento delle opzioni
    stringa_quiz.sort()
    #componimento della domanda con le opzioni
    quiz = ''
    for s in stringa_quiz:
        quiz += s + '\n'

    #Kanji da indovinare
    print('Kanji ', random_option[0][1][1], ':\n')
    #Opzioni
    print(quiz)
    #
    answer = input("Seleziona l'opzione corretta: ")
    if answer == random_option[0][0]:
        score += 1
    else:
        lista_errori.append(random_option[0][1])

end = time.time()
print('Punteggio: ', score, '/', n_quiz)
print('Hai impiegato: ', round(end-start, 0), 'secondi')
for x in lista_errori:
    print(x[0], x[1])
