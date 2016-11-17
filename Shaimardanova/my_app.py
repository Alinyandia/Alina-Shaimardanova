import datetime
import io, json

from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    urls =  {"посмотреть все результаты" : url_for('result'),
             "json" : url_for('json'),
             "поиск" : url_for('form')}
    return render_template('start.html', urls=urls)

@app.route('/thankyou')
def thanks():
    urls = {"посмотреть все результаты" : url_for('result'),
             "вернуться к анкете" : url_for('index')
            }
    answer1 = request.args['answer1']   
    answer2 = request.args['answer2']
    answer3 = request.args['answer3']
    answer4 = request.args['answer4']
    answer5 = request.args['answer5']
    answer6 = request.args['answer6']
    s = '1.' + answer1 + '\t' + '2.'+ answer2 + '\t' + '3.' + answer3 + '\t' + '4.' + answer4 + '\t' + '5.' + answer5 + '\t' +'6.' + answer6  
    out = open('results.txt', 'a', encoding = 'utf-8')
    out.write(s + '\t')
    out.close()
# У меня всё работало, потом я открыла программу ещё раз и оно престало работать. Причину я так и не обнаружила, поэтому оставила старый код. 
#    f = open('results.json', 'a', encoding = 'utf-8') 
#    s1 = json.dumps(request.args, out, ensure_ascii = False)    
#    f.write(s1 + '\t')
#    f.close()

    return render_template('thankyou.html', urls=urls)
    
@app.route('/stats')
def result():
    urls =  {"вернуться к анкете" : url_for('index') } 
    out = open('results.txt', 'r', encoding = 'utf-8')
    string = out.read()
    array = string.split()
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    ar1 = {}
    ar2 = {}
    ar3 = {}
    ar4 = {}
    ar5 = {}
    ar6 = {}
    for word in array:
        if word.startswith('1'):
            a1.append(word[2:])
        if word.startswith('2'):
            a2.append(word[2:])
        if word.startswith('3'):
            a3.append(word[2:])
        if word.startswith('4'):
            a4.append(word[2:])
        if word.startswith('5'):
            a5.append(word[2:])
        if word.startswith('6'):
            a6.append(word[2:])
    for word1 in a1:        
        if word1 in ar1:
            ar1[word1] +=1
        else:
           ar1[word1] = 1

    for word2 in a2:        
        if word2 in ar2:
            ar2[word2] +=1
        else:
           ar2[word2] = 1

    for word3 in a3:        
        if word3 in ar3:
            ar3[word3] +=1
        else:
           ar3[word3] = 1

    for word4 in a4:        
        if word4 in ar4:
            ar4[word4] +=1
        else:
           ar4[word4] = 1

    for word5 in a5:        
        if word5 in ar5:
            ar5[word5] +=1
        else:
           ar5[word5] = 1

    for word6 in a6:        
        if word6 in ar6:
            ar6[word6] +=1
        else:
           ar6[word6] = 1

    d = dict(list(ar1.items())+list(ar2.items()) + list(ar3.items()) + list(ar4.items()) + list(ar5.items()) + list(ar6.items()))
    out.close()
    
    return render_template('results.html', ar1=ar1, ar2=ar2, ar3=ar3, ar4=ar4, ar5=ar5, ar6=ar6, urls=urls)
#    return d

@app.route('/json')
def json():
    urls =  {"посмотреть все результаты" : url_for('result'),
             "вернуться к анкете" :url_for('index')} 
    f = open('results.json', 'r')
    string = f.read()
    f.close()
    return render_template('json.html', string = string, urls=urls)

@app.route('/search')
def form():
    return render_template('question.html')
    
@app.route('/results')
def results():
    urls =  { "вернуться к анкете" :url_for('index')} 
    global d
    lang = request.args['lang']
    for word in d:
        if word == lang:
            return render_template('answer.html', word=word) 
      
                
  
        
if __name__ == '__main__':
    app.run(debug=True)
