import json

import requests

import translate

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def search_music(s):
    url = f'http://cloud-music.pl-fe.cn/search?keywords={s}'
    strhtml = requests.get(url, headers=headers)
    date1 = json.loads(strhtml.text)
    a = date1['result']["songs"]
    c = 0
    search_music_ = []
    for i in a:
        c += 1
        print(c, " :" + str(
            f"""'id':"{str(i['id'])}"'作者':"{i['artists'][0]['name']}"'专辑':"{i['album']['name']}"'专辑id':"{str(i['album']['id'])}"'name':"{i['name']}/"""))
        cee = f""" 'id':{str(i['id'])},'作者':"{i['artists'][0]['name']}",'专辑':"{i['album']['name']}",'专辑id':{str(i['album']['id'])},'name':"{i['name']}" """
        search_music_.append(cee)
    return search_music_


def find_lyric(id: int):
    url = f'http://cloud-music.pl-fe.cn/lyric?id={id}'
    strhtml = requests.get(url, headers=headers).text  # Get方式获取网页数据
    try:
        _date = json.loads(strhtml)
        return _date["lrc"]["lyric"] + _date["tlyric"]["lyric"]
    except Exception as e:
        return _date["lrc"]["lyric"]


def proj():  # 启动
    music_name = input("请输入歌名(number_search : n-s)：")
    if music_name == "n-s":
        number_search = int(input("请输入数字："))
        number_lrc = find_lyric(number_search)
        with open(music_name + '.lrc', 'w', encoding='utf-8') as f:
            f.write(number_lrc)
        print("ok")
    else:
        search_music_str = search_music(music_name)
        a = input("请选择：")
        search_music_dict = eval("{" + search_music_str[int(a) - 1] + "}")
        lrc = find_lyric(int(search_music_dict['id']))
        print(lrc)
        b = input("确定？(y/n)")
        if b == "y":
            with open(music_name + '.lrc', 'w', encoding='utf-8') as f:
                f.write(lrc)
            print("ok")
        else:
            proj()


proj()
