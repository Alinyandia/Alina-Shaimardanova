import urllib.request
import requests
import json
import matplotlib.pyplot as plt
import math
import re
from datetime import date
from collections import Counter

def posts():
    from collections import Counter
    req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=badcomedian&count=100') 
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    posts = data['response'][1:]
    return posts

def info(posts):
    for_graph = open('for_graph.txt', 'a', encoding ='utf-8')
    comments = open('comments.txt', 'a', encoding ='utf-8')
    users = open('users_info.txt', 'a', encoding ='utf-8')
    i = 0 
    for post in posts:
        i += 1
        f = open('posts.json', 'a', encoding ='utf-8')
        f.write(str(post['id']) + ' ' + post['text'] + '\n')
        f.close()
        post_id = post['id']
        link = 'https://api.vk.com/method/wall.getComments?owner_id=-25557243&count=100&post_id=' + str(post_id)
        response = requests.get(link)
        data_com = json.loads(response.text)
        len_c = 0
        k = 0 
        for text in data_com['response'][1:]:
            k += 1
            if k == 100:
                link = 'https://api.vk.com/method/wall.getComments?owner_id=-25557243&count=1&offset=100&post_id=' + str(post_id)
                response1 = requests.get(link)
                data_com = json.loads(response1.text)
                try:
                    len_c += len(text['text'].split())
                    comments.write(str(post['id']) + ' ' + text['text'] + '\n')
                    users.write(str(text['from_id']) + ' ' + str(len(text['text'].split())) + '\n')
                except:
                    continue
            else:
                try:
                    len_c += len(text['text'].split())
                    comments.write(str(post['id']) + ' ' + text['text'] + '\n')
                    users.write(str(text['from_id']) + ' ' + str(len(text['text'].split())) + '\n')
                except:
                    continue
        for_graph.write(str(len(post['text'].split())) + ' ' + str(math.floor(len_c/k)) + '\n')

    for_graph.close()
    users.close()

    return i

def info_100(i):
    for_graph = open('for_graph.txt', 'a', encoding ='utf-8')
    comments = open('comments.txt', 'a', encoding ='utf-8')
    users = open('users_info.txt', 'a', encoding ='utf-8')

    if i == 100:
        req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=badcomedian&count=10&offset=100') 
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        data = json.loads(result)
        posts = data['response'][1:]
        for post in posts:
            i += 1
            f = open('posts.json', 'a', encoding ='utf-8')
            f.write(str(post['id']) + ' ' + post['text'] + '\n')
            f.close()
            post_id = post['id']
            link = 'https://api.vk.com/method/wall.getComments?owner_id=-25557243&count=100&post_id=' + str(post_id)
            response = requests.get(link)
            data_com = json.loads(response.text)
            len_c = 0
            k = 0 
            for text in data_com['response'][1:]:
                k += 1
                if k == 100:
                    link = 'https://api.vk.com/method/wall.getComments?owner_id=-25557243&count=1&offset=100&post_id=' + str(post_id)
                    response1 = requests.get(link)
                    data_com = json.loads(response1.text)
                    try:
                        len_c += len(text['text'].split())
                        comments.write(str(post['id']) + ' ' + text['text'] + '\n')
                        users.write(str(text['from_id']) + ' ' + str(len(text['text'].split())) + '\n')
                    except:
                        continue
                else:
                    try:
                        len_c += len(text['text'].split())
                        comments.write(str(post['id']) + ' ' + text['text'] + '\n')
                        users.write(str(text['from_id']) + ' ' + str(len(text['text'].split())) + '\n')
                    except:
                       continue
            for_graph.write(str(len(post['text'].split())) + ' ' + str(math.floor(len_c/k)) + '\n')

    for_graph.close()
    users.close()

def graph_len():
    i = 0
    l_pos = []
    l_com = []
    with open('for_graph.txt', 'r', encoding ='utf-8') as f:
        text = f.read()
        for k in text.split():
            i += 1
            if i % 2 != 0:
                l_pos.append(k)
            else:
                l_com.append(k)
    post = [int(ple) for ple in l_pos]
    comm = [int(cle) for cle in l_com]
    plt.bar(post, comm)
    plt.title('Соотношение длин постов и комментариев')
    plt.ylabel('Средняя длина комментариев к посту')
    plt.xlabel('Длина поста')
    plt.grid('on')
    plt.show()

def users():
    city = {}
    bida= {}
    i = 0
    k = 0
    b = 0
    users = open('users_info.txt','r', encoding ='utf-8')
    f = users.read()
    for person in f.split():
        i += 1
        if i % 2 != 0:
            link = 'https://api.vk.com/method/users.get?user_id=' + str(person) + '&fields=city,bdate'
            response = requests.get(link)
            data = json.loads(response.text)
            for c in data['response']:
                if 'city' in c:
                    if c['city'] in city:
                        city[c['city']].append(f.split()[k+1])
                        k += 2
                    else:
                        city[c['city']] = list()
                        city[c['city']].append(f.split()[k+1])                        
                        k += 2
                if 'bdate' in c:
                    year = re.search('([0-9]*?)\.([0-9]*?)\.([0-9]*)', c['bdate'])
                    if year:
                        today = date.today()
                        age = today.year - int(year.group(3))
                        if today.month < int(year.group(2)):
                            age -= 1
                        elif today.month == int(year.group(3)) and today.day < int(year.group(1)):
                            age -= 1
                        if age in bida:
                            bida[age].append(f.split()[b+1])
                            b += 2
                        else:
                            bida[age] = list()
                            bida[age].append(f.split()[b+1])                        
                            b += 2
                    else:
                        continue   
    return city, bida

def for_city_gr(city):
    new = open('city.txt', 'a', encoding ='utf-8')
    for elem in city:
        len_c = 0
        k = 0
        for memb in city[elem]:
            len_c = int(len_c) + int(''.join(memb))
            k += 1
        new.write(str(elem) + ' ' + str(math.floor(len_c/k)) + '\n')
    new.close()

def for_bd_gr(bida):
    new = open('bd.txt', 'a', encoding ='utf-8')
    for elem in bida:
        len_c = 0
        k = 0
        for memb in bida[elem]:
            len_c = int(len_c) + int(''.join(memb))
            k += 1
        new.write(str(elem) + ' ' + str(math.floor(len_c/k)) + '\n')
    new.close()
   
def graph_city():
    i = 0
    mem_c = []
    l_com = []
    with open('city.txt', 'r', encoding ='utf-8') as f:
        text = f.read()
        for k in text.split():
            i += 1
            if i % 2 != 0:
                mem_c.append(k)
            else:
                l_com.append(k)
    l_com.sort()
    mem_c.sort()
    city = [int(ple) for ple in mem_c]
    comm = [int(cle) for cle in l_com]
    plt.bar(comm, city)
    plt.xticks(comm, city)
    plt.title('Город vs Длинна комментриев')
    plt.ylabel('Средняя длина комментариев к посту')
    plt.xlabel('Город автора')
    plt.grid('on')
    plt.show()

def graph_age():
    i = 0
    age_c = []
    l_com = []
    with open('bd.txt', 'r', encoding ='utf-8') as f:
        text = f.read()
        for k in text.split():
            i += 1
            if i % 2 != 0:
                age_c.append(k)
            else:
                l_com.append(k)
    l_com.sort()
    age_c.sort()
    age = [int(ple) for ple in age_c]
    comm = [int(cle) for cle in l_com]
    plt.bar(comm, age)
    plt.xticks(comm, age)
    plt.title('Возраст vs Длинна комментриев')
    plt.xlabel('Средняя длина комментариев к посту')
    plt.ylabel('Возраст автора')
    plt.grid('on')
    plt.show()

def main():
#    a = posts()
#    b = info(a)
#    c = info_100(b)
#    d = graph_len()
#    e, f = users()
#    g = for_city_gr(e)
#    h = for_bd_gr(f)
    i = graph_city()
    g = graph_age()
if __name__== '__main__':
    main() 
