import random
#import os

WORDS = ['skillfactory','testing','blackbox','pytest']
word = WORDS[random.randrange(len(WORDS))]
output = ('_'*len(word))
answers = []
wrong_answers = 4
#clear = lambda: os.system('clear')

def check(word, letter):
    result=[]
    for i in range(0,len(word)):
        if letter == word[i]:
            result.append(i)
    return result

def show_word(output,letters,letter):
    output = list(output)
    for i in letters:
        output[i]=letter
    return (''.join(output))

def check_input(letter,answers):
    if len(letter)>1:
        print ('\n',"Введите 1 букву")
        return False
    if letter in answers:
        print('\n',"Вы уже вводили букву ", letter, '\n')
        return False
    else:
        return True

def print_scr(output, wrong_answers):
    print('*'*40)
    print('Загаданное слово: ', output)
    print('Осталось попыток: ', wrong_answers )
    print('*'*40)
    print('\n')
#print(word)
#clear()
#print(os.name)
if __name__ == "__main__":
    while wrong_answers > 0:
        print_scr(output,wrong_answers)
        letter = input('Введите букву:')
        if check_input(letter,answers):
            answers.append(letter)
            if len(check(word,letter))>0:
                output = show_word(output,check(word,letter),letter)
                print('\n','Есть такая буква!','\n')
            else:
                print('\n','Не угадали','\n')
                wrong_answers-=1
            if output == word:
                print('Вы угадали слово!')
                break
            else:
                continue
        else:
            continue
    if wrong_answers == 0:
        print ('Вы проиграли')
