import flask
import telebot
import conf
import re
from pymystem3 import Mystem
import pymorphy2
from pymorphy2 import MorphAnalyzer
import random
import json
import ast

morph = MorphAnalyzer()
m = Mystem()


def N_VN(first, result, string):
    num = random.randint(0, len(result[first.tag.POS])-1)
    r = result[first.tag.POS][num]
    new_word = (morph.parse(r))[0]
    for el in new_word.lexeme:
        if el.tag == first.tag:
            string = str(el[0])
    return string


def VERB(first, result, string):
    if first.tag.aspect == 'impf' and first.tag.transitivity == 'intr':
        num1 = random.randint(0, len(result[first.tag.POS]['impf, intr'])-1)
        r1 = result[first.tag.POS]['impf, intr'][num1]
        new_word1 = (morph.parse(r1))[0]
        for el1 in new_word1.lexeme:
            if el1.tag == first.tag:
                string = str(el1[0])
    if first.tag.aspect == 'impf' and first.tag.transitivity == 'tran':
        num2 = random.randint(0, len(result[first.tag.POS]['impf, tran'])-1)
        r2 = result[first.tag.POS]['impf, tran'][num2]
        new_word2 = (morph.parse(r2))[0]
        for el2 in new_word2.lexeme:
            if el2.tag == first.tag:
                string = str(el2[0])
    if first.tag.aspect == 'perf' and first.tag.transitivity == 'tran':
        num3 = random.randint(0, len(result[first.tag.POS]['perf, tran'])-1)
        r3 = result[first.tag.POS]['perf, tran'][num3]
        new_word3 = (morph.parse(r3))[0]
        for el3 in new_word3.lexeme:
            if el3.tag == first.tag:
                string = str(el3[0])
    if first.tag.aspect == 'perf' and first.tag.transitivity == 'intr':
        num4 = random.randint(0, len(result[first.tag.POS]['perf, intr'])-1)
        r4 = result[first.tag.POS]['perf, intr'][num4]
        new_word4 = (morph.parse(r4))[0]
        for el4 in new_word4.lexeme:
            if el4.tag == first.tag:
                string = str(el4[0])
    return string

def anim_NOUN(first, result, string):
    
    if first.tag.gender == 'masc':
        num5 = random.randint(0, len(result[first.tag.POS]['anim']['masc'])-1)
        r5 = result[first.tag.POS]['anim']['masc'][num5]
        new_word5 = (morph.parse(r5))[0]
        for el5 in new_word5.lexeme:
            if el5.tag == first.tag:
                string = str(el5[0])
    if first.tag.gender == 'neut':
        num6 = random.randint(0, len(result[first.tag.POS]['anim']['neut'])-1)
        r6 = result[first.tag.POS]['anim']['neut'][num6]
        new_word6 = (morph.parse(r6))[0]
        for el6 in new_word6.lexeme:
            if el6.tag == first.tag:
                string = str(el6[0])
    if first.tag.gender == 'femn':
        num7 = random.randint(0, len(result[first.tag.POS]['anim']['femn'])-1)
        r7 = result[first.tag.POS]['anim']['femn'][num7]
        new_word7 = (morph.parse(r7))[0]
        for el7 in new_word7.lexeme:
            if el7.tag == first.tag:
                string = str(el7[0])
    return string

def inan_NOUN(first, result, string):

    if first.tag.gender == 'masc':
        num8 = random.randint(0, len(result[first.tag.POS]['inan']['masc'])-1)
        r8 = result[first.tag.POS]['inan']['masc'][num8]
        new_word8 = (morph.parse(r8))[0]
        for el8 in new_word8.lexeme:
            if el8.tag == first.tag:
                string = str(el8[0])
    if first.tag.gender == 'neut':
        num9 = random.randint(0, len(result[first.tag.POS]['inan']['neut'])-1)
        r9 = result[first.tag.POS]['inan']['neut'][num9]
        new_word9 = (morph.parse(r9))[0]
        for el9 in new_word9.lexeme:
            if el9.tag == first.tag:
                string = str(el9[0])
    if first.tag.gender == 'femn':
        num0 = random.randint(0, len(result[first.tag.POS]['inan']['femn'])-1)
        r0 = result[first.tag.POS]['inan']['femn'][num0]
        new_word0 = (morph.parse(r0))[0]
        for el0 in new_word0.lexeme:
            if el0.tag == first.tag:
                string = str(el0[0])
    return string
    

k = open('пробник1.txt', 'r', encoding ='utf-8')
d = k.read()
result = ast.literal_eval(d)
string = ''
for word in message:
    word = word.strip('\.?,:!')
    ana = morph.parse(word)
    first = ana[0]
    if first.tag.POS != 'VERB' and first.tag.POS != 'NOUN':
        string += N_VN(first, result, string) + ' '
    if first.tag.POS == 'VERB':
        string += VERB(first, result, string) + ' '
    if first.tag.POS == 'NOUN':
        if first.tag.animacy == 'anim':
            string += anim_NOUN(first, result, string) + ' '
        if first.tag.animacy == 'inan':
            string += inan_NOUN(first, result, string) + ' '


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Ну здравствуйте! Что расскажете мне?")


@bot.message_handler(func=lambda m: True)
def send_len(message):
	bot.send_message(message.chat.id, string)


if __name__ == '__main__':
    bot.polling(none_stop=True)
