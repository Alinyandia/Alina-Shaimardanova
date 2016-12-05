import urllib.request
import re

html_url1 = ['http://calendar.fontanka.ru/articles/4624']
html_url = ['https://www.gazeta.ru/culture/news/2016/12/01/n_9401249.shtml']
html_url2 = ['https://regnum.ru/news/cultura/2212635.html']
html_url3 = ['https://life.ru/t/%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B0/940040/chielovieka-amfibiiu_pieriesnimut_spietsialno_dlia_kitaia']

def regnum():
    for i in html_url2:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request( i, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            reg_url = re.compile('<b class="regnum_title">REGNUM</b></span>(.*?)</div>', flags=re.U | re.DOTALL)
            text = reg_url.findall(html)
            text = ''.join(text).lower()
            reg_clean = re.compile('\n|&nbsp;|</p>|<p>|&laquo;|&raquo;|\.|,|\(|\)|;|:', flags=re.U | re.DOTALL)
            clean_text = reg_clean.sub(' ', "".join(text))
            text_regnum = clean_text.split()
            regnum = set(text_regnum)
    return regnum, clean_text

def fontanka():
    for i in html_url1:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request( i, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('windows-1251')
            reg_url = re.compile('<!--extra_microicons newsphoto -->(.*?)<p>Фонтанка.ру</p>', flags=re.U | re.DOTALL)
            text = reg_url.findall(html)
            text = ''.join(text).lower()
            reg_clean = re.compile('\n|&nbsp;|</p>|<p>|&laquo;|&raquo;|\.|,|\(|\)|&ndash|;|:', flags=re.U | re.DOTALL)
            clean_text = reg_clean.sub(' ', "".join(text))
            text_font = clean_text.split()
            font = set(text_font)
    return font, clean_text

def ru():
    for i in html_url:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request( i, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('windows-1251')
            reg_url = re.compile('<div style="height: 20px"></div><p>(.*?)</p> </div>', flags=re.U | re.DOTALL)
            text = reg_url.findall(html)
            text = ''.join(text).lower()
            reg_clean = re.compile('&laquo;|&raquo;|<a href=http://ria.ru target=_blank><b>|</b></a>|</p><p>|«|»|\.|,|;|:', flags=re.U | re.DOTALL)
            clean_text = reg_clean.sub('', "".join(text))
            text_ru = clean_text.split()
            ru = set(text_ru)
    return ru, clean_text

def life():
    for i in html_url3:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request( i, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            reg_url = re.compile('<div class=\"content-note\" itemprop=\"text"><p><span>(.*?)</span></p></div>', flags=re.U | re.DOTALL)
            text = reg_url.findall(html)
            text = ''.join(text).lower()
            reg_clean = re.compile('\.|,|\"|<p>|<span>|</span>|</p>|\)|—|\(', flags=re.U | re.DOTALL)
            clean_text = reg_clean.sub('', "".join(text))
            text_life = clean_text.split()
            life = set(text_life)
    return life, clean_text
        

def inter(regnum, font, ru, life):
    array = []
    res1 = regnum.intersection(font)
    res2 = res1.intersection(ru)
    res3 = res2.intersection(life)
    f = open('Перечесения.txt', 'a', encoding = 'utf-8')
    for i in res2:
        array.append(i)
    array.sort()
    for word in array:
        f.write(word + '\n')    
    f.close()


def sym_dif(regnum, font, ru, life):
    array = []
    res1 = regnum.symmetric_difference(font)
    res2 = res1.symmetric_difference(ru)
    res3 = res2.symmetric_difference(life) 
    f = open('Разность.txt', 'a', encoding = 'utf-8')
    for i in res3:
        array.append(i)
    array.sort()
    for word in array:
        f.write(word + '\n')    
    f.close()

def ten(t1, t2, t3, t4):
    d = {}
    f = open('Разность.txt', 'r', encoding = 'utf-8')
    text = f.read()
    t = (t1 + ' ' + t2 + ' ' + t3 + ' ' + t4).split()
    for word in t:
        if word in text:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    k = open('Частотные_словоформы.txt', 'a', encoding = 'utf-8')
    for word in d:
        if d[word] > 1:
            k.write(str(word) + '\n')
    k.close()
    f.close()

def main():
    a,t1 = regnum()
    b,t2 = fontanka()
    c,t3 = ru()
    r,t4 = life()
    d = inter(a,b,c,r)
    e = sym_dif(a,b,c,r)    
    k = ten(t1,t2,t3,t4)
if __name__== '__main__':
    main()
