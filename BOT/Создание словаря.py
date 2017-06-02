mport re
from pymystem3 import Mystem
import pymorphy2
from pymorphy2 import MorphAnalyzer
import random
import json
import ast

morph = MorphAnalyzer()
m = Mystem()

def f():
    f = open('/Users/alinashaymardanova/Desktop/bot заменяющий слова на аналогичные/1grams-3.txt', 'r', encoding = 'utf-8')
    words = f.readlines()
    lex = []
    for word in words:
        res = re.search('([0-9]*?)\t(([а-я]|[А-Я])*?)\n', word)
        if res:
            lex.append(res.group(2))
    return lex

def s(lex):   
    result = {}
    for word in lex:
        ana = morph.parse(word)
        first = ana[0]
        tags = first.tag
        if first.tag.POS != 'VERB' and first.tag.POS != 'NOUN':
            if first.tag.POS in result:
                result[first.tag.POS].append(first.normal_form)
            else:
                result[first.tag.POS] = list()
                result[first.tag.POS].append(first.normal_form)

        if first.tag.POS == 'VERB' first.tag.POS == 'INF':
            if first.tag.POS not in result:
                result[first.tag.POS] = dict()
                continue
            if first.tag.aspect == 'impf' and first.tag.transitivity == 'tran':
                if 'impf, tran' in result[first.tag.POS]:
                    result[first.tag.POS]['impf, tran'].append(first.normal_form)
                else:
                    result[first.tag.POS]['impf, tran'] = list()
                    result[first.tag.POS]['impf, tran'].append(first.normal_form)

            elif first.tag.aspect == 'perf' and first.tag.transitivity == 'tran':
                if 'perf, tran' in result[first.tag.POS]:
                    result[first.tag.POS]['perf, tran'].append(first.normal_form)
                else:
                    result[first.tag.POS]['perf, tran'] = list()
                    result[first.tag.POS]['perf, tran'].append(first.normal_form)

            elif first.tag.aspect == 'perf' and first.tag.transitivity == 'intr':
                if 'perf, intr' in result[first.tag.POS]:
                    result[first.tag.POS]['perf, intr'].append(first.normal_form)
                else:
                    result[first.tag.POS]['perf, intr'] = list()
                    result[first.tag.POS]['perf, intr'].append(first.normal_form)

            elif first.tag.aspect == 'impf' and first.tag.transitivity == 'intr':
                if 'impf, intr' in result[first.tag.POS]:
                    result[first.tag.POS]['impf, intr'].append(first.normal_form)
                else:
                    result[first.tag.POS]['impf, intr'] = list()
                    result[first.tag.POS]['impf, intr'].append(first.normal_form)

        if first.tag.POS == 'NOUN':
            if first.tag.POS not in result:
                result[first.tag.POS] = dict()
                continue
            if first.tag.animacy == 'anim':
                if 'anim' not in result[first.tag.POS]:
                    result[first.tag.POS]['anim'] = dict()
                    continue
                if first.tag.gender == 'masc':
                    if 'masc' in result[first.tag.POS]['anim']:
                        result[first.tag.POS]['anim']['masc'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['anim']['masc'] = list()
                        result[first.tag.POS]['anim']['masc'].append(first.normal_form)
                if first.tag.gender == 'femn':
                    if 'femn' in result[first.tag.POS]['anim']:
                        result[first.tag.POS]['anim']['femn'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['anim']['femn'] = list()
                        result[first.tag.POS]['anim']['femn'].append(first.normal_form)

                if first.tag.gender == 'neut':
                    if 'neut' in result[first.tag.POS]['anim']:
                        result[first.tag.POS]['anim']['neut'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['anim']['neut'] = list()
                        result[first.tag.POS]['anim']['neut'].append(first.normal_form)

            if first.tag.animacy == 'inan':
                if 'inan' not in result[first.tag.POS]:
                    result[first.tag.POS]['inan'] = dict()
                    continue
                if first.tag.gender == 'masc':
                    if 'masc' in result[first.tag.POS]['inan']:
                        result[first.tag.POS]['inan']['masc'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['inan']['masc'] = list()
                        result[first.tag.POS]['inan']['masc'].append(first.normal_form)
                if first.tag.gender == 'femn':
                    if 'femn' in result[first.tag.POS]['inan']:
                        result[first.tag.POS]['inan']['femn'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['inan']['femn'] = list()
                        result[first.tag.POS]['inan']['femn'].append(first.normal_form)

                if first.tag.gender == 'neut':
                    if 'neut' in result[first.tag.POS]['inan']:
                        result[first.tag.POS]['inan']['neut'].append(first.normal_form)
                    else:                       
                        result[first.tag.POS]['inan']['neut'] = list()
                        result[first.tag.POS]['inan']['neut'].append(first.normal_form)
                       
                        
    file = open("пробник.txt", 'w', encoding ='utf-8')
    file.write(str(result)) 
    file.close()
    return result
