import re
import os


def search():
    f = open('text.txt', 'r', encoding = 'utf-8')
    f1 = open('gazeta.html', 'r', encoding = 'utf-8')
    f2 = open('wordlist.txt', 'a', encoding = 'utf-8')
    reg_clean = re.compile('\ӏ',flags=re.U | re.DOTALL) # так как программа принимает | за разделитель
    text = f.read()
    clean_text = reg_clean.sub('л', text)
    html = f1.read()
    array = clean_text.split()
    for word in array:
        if word in html:
            f2.write(word + '\n')
    f.close()
    f1.close()
    f2.close() 

def ms():
    d = {}
    os.system(r"/Users/alinashaymardanova/Documents/mystem /Users/alinashaymardanova/Desktop/text.txt /Users/alinashaymardanova/Desktop/result.txt -ni")
    f = open('result.txt', 'r', encoding = 'utf-8')
    f1 = open('rus_nouns.txt', 'a', encoding = 'utf-8')
    text = f.readlines()
    for line in text:
        reg = re.compile('(.*?)\{(.[^\?]*?)=S\,[а-я]*?=им,мн.*?\}', flags=re.U | re.DOTALL)
        r = reg.search(line)
        if r:
            token = r.group(1)
            if token not in d:
                d[token] = r.group(2)
    for word in d:
        f1.write(word + '\n')
        print(word, d[word] + '\n')

    return d       
        
    
def db(d): # видимо, я пошла не по самому рациональному пути, поэтому я не успела создать файл с INSERT'ами
    f = open('sql.txt', 'a', encoding = 'utf-8')
    for word in d:
        r = re.compile('([а-я]*?)=S', str(d[word]))
        f.write('INSERT INTO rus_words (wordform, lemma) VALUES (\"'+ str(word) + '\", \"' + str(r.group(1)) + '\");' + '\n')
    f.close()
    
def main():
    a = search()
    b = ms()
    c = db(b)

if __name__== '__main__':
    main()
