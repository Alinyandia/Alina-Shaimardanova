import urllib.request
import html
import re
import time
import os

os.system(r'/Users/alinashaymardanova/Desktop/Новая_папка/Num1.py')
os.chdir('/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа')

def work_with_text():
    i = 142
    f = open('pages.txt')
    for line in f:
        i+=1
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request( line, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            reg_title = re.compile('<div class="itemIntroText">(.*?)</div>',flags=re.U | re.DOTALL)
            reg_ftext = re.compile('<div class="itemFullText">(.*?)</div>',flags=re.U | re.DOTALL)
            reg_date = re.compile('<div class="itemDateCreated">(.*?)</div>', flags=re.U | re.DOTALL)
            reg_year = re.compile('[0-9]*?\.[0-9]*?\.([0-9]*?) ', flags=re.U | re.DOTALL)
            reg_month = re.compile('[0-9]*?\.([0-9]*?)\.', flags=re.U | re.DOTALL)
            reg_clean = re.compile('\n|\t|\r|\xa0|</p>|<p>|<p style="text-align: left;">|<p style="text-align: right;">', flags=re.U | re.DOTALL)
            title = reg_title.findall(html)
            text = reg_ftext.findall(html)
            date = reg_date.findall(html)
            clean_text = reg_clean.sub('', "".join(text))
            clean_title = reg_clean.sub('', "".join(title))
            clean_date = reg_clean.sub('', "".join(date))
            stext = ''.join(clean_text)
            stitle = ''.join(clean_title)
            sdate = ''.join(clean_date)
            year = reg_year.findall(clean_date)
            month = reg_month.findall(clean_date)
            row = "газета_Победа/plain/%s/%s\tNoname\t\t\t\t\t%s\t%s\tПублицистика\t\t\t\t\tNotopic\t\t\tНейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\tГазета 'Победа'\t\t\t%s\tгазета\tРоссия\tУдмуртия\tru"
            csv = open('Metadata.csv', 'a', encoding = 'utf - 8')
            csv.write(row %("".join(year), "".join(month), clean_title, clean_date, line, "".join(year)))
            csv.close()
            
            if not os.path.exists('plain'):
                os.mkdir('plain')
                os.chdir('plain')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+str(i)+'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+str(i)+'.txt', 'w', encoding = 'utf - 8')
                        newf.close()
            else:
                os.chdir('plain')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+str(i)+'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+str(i)+'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+str(i)+'.txt', 'w', encoding = 'utf - 8')                    
                        newf.write(clean_text)
                        newf.close()
            os.chdir('/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа')

            if not os.path.exists('mystem-xml'):
                os.mkdir('mystem-xml')
                os.chdir('mystem-xml')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
            else:
                os.chdir('mystem-xml')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()                   
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
            os.chdir('/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа')
            
            if not os.path.exists('mystem-plain'):
                os.mkdir('mystem-plain')
                os.chdir('mystem-plain')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
            else:
                os.chdir('mystem-plain')
                if not os.path.exists(''.join(year)):
                    os.makedirs(''.join(year))
                    os.chdir(''.join(year))
                    os.makedirs(''.join(month))
                    os.chdir(''.join(month))
                    newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                    newf.write(clean_text)
                    newf.close()
                else:
                    os.chdir(''.join(year))
                    if not os.path.exists(''.join(month)):
                        os.makedirs(''.join(month))
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                    else:
                        os.chdir(''.join(month))
                        newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
                        newf.write(clean_text)
                        newf.close()
                        
            inp = "/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа/plain/" + "".join(year) + "/" + "".join(month) + "/" + "статья"+ str(i) + ".txt"
            out_xml = "/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа/mystem-xml/" + "".join(year) + "/" + "".join(month) + "/" + "статья"+ str(i) + ".txt"
            out_text = "/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа/mystem-plain/" + "".join(year) + "/" + "".join(month) + "/" + "статья"+ str(i) + ".txt"
            os.system(r"/Users/alinashaymardanova/Downloads/mystem " + inp + " " + out_xml + " -cnid --format xml --eng-gr")
            os.system(r"/Users/alinashaymardanova/Downloads/mystem " + inp + " " + out_text + " -cnid --format text --eng-gr")
            os.chdir('/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа/plain/' + "".join(year) + "/" + "".join(month))
            newf = open('статья'+ str(i) +'.txt', 'w', encoding = 'utf - 8')
            newf.write('@au' + ' ' + 'Noname' + '\n' + '@ti' + ' ' + clean_title + '\n' + '@da' + ' ' + clean_date + '\n' + '@url' + ' ' + line + '\n' + clean_text)
            newf.close()
            os.chdir('/Users/alinashaymardanova/Desktop/Новая_папка/газета_Победа')
            time.sleep(6)
    
def main():
    a = work_with_text()

if __name__== '__main__':
    main()
