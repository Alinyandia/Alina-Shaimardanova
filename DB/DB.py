import re
import os

def clean_t():
    f = open('text.txt', 'r', encoding = 'utf-8')
    l_text = f.read()
    text = l_text.lower()
    reg_clean = re.compile('\.|\,|:|;', flags=re.U | re.DOTALL)
    clean_text = reg_clean.sub('', text)
    cl_text = reg_clean.sub('', l_text)
    return clean_text, cl_text

def symb():
    ar = []
    r = ''  
    f = open('text.txt', 'r', encoding = 'utf-8')
    i = 0
    text = f.read()
    array = text.split()
    reg_l = re.compile('(\.|\,|\"|!|\?|:|;)', flags=re.U | re.DOTALL)
    while i <= (len(array)-1):
        if i != 0:
            right = reg_l.findall(array[i])
            if right:
                left = reg_l.findall(array[i-1])
                if left:
                    l = ''.join(left)
                    r = ''.join(right)
                    i += 1
                else:
                    left = 0
                    l = str(left)
                    r = ''.join(right)
                    i += 1
            else:
                rigth = 0
                left = reg_l.findall(array[i-1])
                if left:
                    l = ''.join(left)
                    r = '0'              
                    i += 1
                else:
                    left = 0
                    l = '0'
                    r = '0'
                    i += 1                
        else:
            left = 0
            right = reg_l.findall(array[i])
            if right:
                l = '0'
                r = ''.join(right)
                i += 1
            else:
                l = '0'
                r = '0'
                i += 1 
        ar.append(l)
        ar.append(r)

    return ar

def db(clean_text):
    d = {}
    i = 1
    array = clean_text.split()
    f = open('result.txt', 'a', encoding = 'utf-8')
    open('result_ms.txt', 'a', encoding = 'utf-8')
    for word in array:
        os.system(r"/Users/alinashaymardanova/Documents/mystem text.txt result_ms.txt -n")
    f1 = open('result_ms.txt', 'r', encoding = 'utf-8')
    string = f1.readlines()
    for line in string:
        reg_lemma = re.compile('(.*?){(.*?)}', flags=re.U | re.DOTALL)
        r = reg_lemma.search(line)
        token = r.group(1)
        token = token.lower()
        if token not in d:
            d[token] = r.group(2)
        else:
            continue
    for word in d:
        f.write('INSERT INTO Tokens (ID, Token, Lemma) VALUES (\"'+ str(i) +'\", \"'+ word +'\", \"' + d[word] + '\");' + '\n')
        d[word] = i
        i += 1
    f.close()
    f1.close()
    return d

def db2(cl_text, d, ar):
    l = 0
    i = 1
    array = cl_text.split()
    f = open('result.txt', 'a', encoding = 'utf-8')
    for word in array:
        for word1 in d:
            if word.lower() == word1:
                f.write('INSERT INTO Text (ID, Token, token_num, symb_left,  symb_right, token_id) VALUES (\"'+ str(i) +'\", \"'+ word +'\", \"' + str(i) +'\", \"' + ar[l] + '\", \"' + ar[l+1] + '\", \"' + str(d[word1]) + '\");' + '\n')
                i += 1
            else:
                continue
        l += 2       
    
def main():
    a,b = clean_t()
    x = symb()
    c = db(a)
    d = db2(b,c,x)
if __name__== '__main__':
    main()
