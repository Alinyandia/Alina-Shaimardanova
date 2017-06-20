import flask
import telebot
import urllib.request
import os
import requests
import json
import matplotlib.pyplot as plt
import networkx as nx
import re
from pymystem3 import Mystem
import time
import random
import stickers


TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN, threaded=False)

bot.remove_webhook()
bot.set_webhook(url="https://boiling-waters-89250.herokuapp.com/bot")

app = flask.Flask(__name__)


def first(k):
    text = ''
    l = 0
    if not k.isdigit():
        req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=' + str(k) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de')
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        data = json.loads(result)
        if data['response'][0] >= 400:
            while l != 400:
                i = 0
                req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=' + str(k) + '&count=100&offset=' + str(l) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de') 
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                data = json.loads(result)
                time.sleep(0.15)
                while i != 100:
                    i += 1
                    text = text + str(data['response'][i]['text']) + '\n'
                l += 100
        else:
            while l < data['response'][0]-10:
                i = 0
                req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=' + str(k) + '&count=10&offset=' + str(l) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de') 
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                data = json.loads(result)
                time.sleep(0.15)
                while i != 10:
                    i += 1
                    text = text + str(data['response'][i]['text']) + '\n'
                l += 10 

    else:
        req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=' + str(k) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de')
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        data = json.loads(result)
        if data['response'][0] >= 400:
            while l != 400:
                i = 0
                req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=' + str(k) + '&count=100&offset=' + str(l) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de') 
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                data = json.loads(result)
                time.sleep(0.15)
                while i != 100:
                    i += 1
                    text = text + str(data['response'][i]['text']) + '\n'
                l += 100
        else:
            while l < data['response'][0]-10:
                i = 0
                req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=' + str(k) + '&count=10&offset=' + str(l) + '&access_token=04e61db0115fc8c56c38a0f5f1acc3b6e243bd8c6cf711a5e0c7fdae781511fe983a6cb27e8969788e3de') 
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                data = json.loads(result)
                time.sleep(0.15)
                while i != 10:
                    i += 1
                    text = text + str(data['response'][i]['text']) + '\n'
                l += 10
    return text

def clean(text):
    text = re.sub(r'\:|\)|<br>|<r>|\$|\(|\,|D|3|\>|\<|\{|\}|\"|\*|\_|\^|\=|\#|\“|\@|\\|\/|\♥|\❤|\☺', ' ', text)
    text = text.lower()
    res = []
    for i in text.split('\n'):
        for part in i.replace('!', '.').replace('?', '.').split('.'):
            if part != '':
                res.append(part + '\n')
    return res

def info(res):
    for_graph = []
    m = Mystem()
    for el in res:
        s = ''
        try:
            for el1 in el.split():
                ana = m.analyze(el1)
                for word in ana:
                    if 'analysis' in word:
                        gr = word['analysis'][0]['gr']
                        pos = gr.split('=')[0].split(',')[0]
                        if pos != 'CONJ' and pos != 'INTJ' and pos != 'PART' and pos != 'PR' and pos != 'ADVPRO' and pos != 'APRO' and pos != 'SPRO':
                            s = s + word['text'] + ' '
                            
        except:
            continue
        for_graph.append(s)

    return for_graph

def graph(for_graph):
    G = nx.Graph() 
    edge=[]
    for el in for_graph:
        i = 0
        ele = el.split()
        if len(ele) == 1:
            if ele[i] not in G:
                G.add_node(ele[i])
        if len(ele) == 2:
            if ele[i] not in G:
                G.add_node(ele[i])
            if ele[i+1] not in G:
                G.add_node(ele[i+1])
            edge.append((ele[i], ele[i+1]))
        if len(ele) > 2:
            while i != len(ele)-2:
                if ele[i] not in G:
                    G.add_node(ele[i])
                if ele[i+1] not in G:
                    G.add_node(ele[i+1])
                if ele[i+2] not in G:
                    G.add_node(ele[i+2])
                edge.append((ele[i], ele[i+1]))
                edge.append((ele[i], ele[i+2]))
                edge.append((ele[i+1], ele[i+2]))
                i += 1
    G.add_edges_from(edge)
    pos=nx.spring_layout(G)
    plt.title("Ваш граф")
    #nx.draw_networkx_nodes(G, pos, node_color='green', node_size=10)
    #nx.draw_networkx_edges(G, pos, edge_color='yellow')
    #plt.savefig('/home/alinyandiaa/mysite/__pycache__/1.png')
    #plt.axis('off')
    #plt.show()
    s = ''
    if G.number_of_nodes() == 0 :
        s = 'Кажется, кто-то тут жмотит свою стену для меня:) (и это вот этот человек, сообщением выше)'
    else:
        s = "Вот некоторая инфа о полученном графе:" + '\n'+ 'Количество узлов (слов):' + ' ' + str(G.number_of_nodes()) + '\n' + 'Количество рёбер:' + ' ' + str(G.number_of_edges()) + ' ' + '(подсказка: если узлы-слова соединены ребрами, значит такие слова стоят рядом)' + '\n' + 'Список самых популярных слов:' + '\n'
        k = 0
        deg = nx.degree_centrality(G)
        for nodeid1 in sorted(deg, key=deg.get, reverse=True): 
            k += 1
            s = s + '✬' + ' ' + '\"' + str(nodeid1) + '\"' + ' ' + 'имеет различных соседей в количестве:' + ' ' + str(G.degree(nodeid1)) + '\n'
            if k == 10:
                break
    return s

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Ну здравствуйте!\n"
	                                  "Меня зовут Граф неДракула бот.\n"
	                                  "Я генерирую яркие графы на основе полнозначных слов со стены пользователя.\n"
                                          "Если хотите узнать побольше о том, что такое графы и с чем их едят, нажмите /help \n"
                                          "Для того, чтобы узнать, какие слова на Вашей стене или стене Вашего друга (брата, мамы...бабушки?) чаще всего встречаются рядом друг с другом, отправьте мне id или короткое имя пользователя в вк.\n"
	                                  "Жду-жду:)")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id,"Граф — абстрактный математический объект, представляющий собой множество вершин графа и набор рёбер, то есть соединений между парами вершин. Например, за множество вершин можно взять множество аэропортов, обслуживаемых некоторой авиакомпанией, а за множество рёбер взять регулярные рейсы этой авиакомпании между городами.")
	bot.send_message(message.chat.id,"Всё ещё непонятно?:(\n"
                                         "Тогда читайте тут и знакомьтесь поближе: https://ru.wikipedia.org/wiki/Граф_(математика)")
                         

@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id, "Так-так, посмотрим, что тут у нас.")
    bot.send_sticker(message.chat.id, random.choice(stickers.vopros))
    try:
        tex = first(message.text)
        res = clean(tex)
        for_graph = info(res)
        s = graph(for_graph)
        bot.send_message(message.chat.id, s)
    except:
        bot.send_message(message.chat.id, 'К сожалению, я не смог найти такого пользователя. Но Вы не отчаивайтесь! (и я не буду)')




@app.route("/bot", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

