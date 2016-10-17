import urllib.request
import time
import os
html = 'http://pobeda2.ru'

if not os.path.exists('газета_Победа'):
    os.mkdir('газета_Победа')
    os.chdir('газета_Победа')
else:
    os.chdir('газета_Победа')

def download_page(pageUrl, f):
    try:
        req = urllib.request.Request(pageUrl)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('ISO-8859-1')
            f.write(pageUrl + '\n')       
    except:
        print ('Error at', pageUrl)
        return
    time.sleep(2)

commonUrl = 'http://pobeda2.ru/component/k2/item/'
for i in range (471, 4389):
    pageUrl = commonUrl + str(i)
    f = open('pages.txt', 'a')
    download_page (pageUrl, f)
