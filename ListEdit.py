import json
from re import S
import string
from os import system, name, fdopen
from time import sleep

class Option:    
    def __init__(self, kanji = '', ita = '', sound = ''):
        self.kanji = kanji
        self.ita = ita
        self.sound = sound

    def set_kanji(self, kanji):
        self.kanji = kanji
    
    def set_ita(self, ita):
        self.ita = ita

    def set_sound(self, sound):
        self.sound = sound

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



if __name__ == '__main__':
    clear()
    kanji_list = []
    #lettura dei dati dal file json
    try:
        f = open('data.json', 'r')
        json_list = json.load(f)
        f.close()
        for element in json_list:
            kanji_list.append(Option(element["kanji"], element["ita"], element["sound"]))
    except:
        print('WARNING: No existing list was found!')
        sleep(2)


    #Ciclo inserimento dei dai
    stop = False

    while(not stop):
        clear()
        if(input("Vuoi un nuovo Kanji alla tua lista? (s,n) \n") == "s"):
            print('Processo di inserimento\n')

            new_kanji = Option()
        
            new_kanji.set_kanji(input('Inserire kanji: '))
            new_kanji.set_ita(input('Inserire traduzione in italiano: '))
            new_kanji.set_sound(input('Inserire rappresentazione suono: '))

            clear()

            #ricapitola i campi che si vogliono inserire
            print('Kanji ', new_kanji.kanji)
            print('Ita ', new_kanji.ita)
            print('Suono ', new_kanji.sound)
            
            if(input('Vuoi aggiungere questo kanjii alla tua lista? (s, n)\n') == 's'):
                kanji_list.append(new_kanji)
            else:
                print('Inserimento annulato!')
                sleep(2)

        else:
            stop = True

    #opzione di visualizzare la lista di kanji
    clear()
    if(input('Vuoi mostrare l\'elenco completo dei kanji?: (s,n)\n') == 's'):
        i = 0
        clear()
        for k in kanji_list:
            print(i, '\t\t', k.kanji, '\t\t', k.ita, '\t\t', k.sound)
            i += 1

        
        if(input('Vuoi eliminare una riga dell\'elenco?: (s,n):\n') == 's'):
            index_str = input('Quale riga vuoi eliminare?\n')
            try:
                index_num = int(index_str)
                if((index_num <=0) or (index_num < len(kanji_list))):
                    kanji_list.pop(index_num)
                    print('Kanji eliminato correttamente')
                else:
                    print('WARNING: il numero selezionato non è presente nella lista')
            except:
                print('WARNING: Inserire il numero di riga')
    #scrittura dei dati sul file json
    f = open('data.json', 'w')
    json.dump([k.__dict__ for k in kanji_list], f, indent=4)
    f.close()