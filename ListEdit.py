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
            
    #scrittura dei dati sul file json
    f = open('data.json', 'w')
    json.dump([k.__dict__ for k in kanji_list], f, indent=4)
    f.close()