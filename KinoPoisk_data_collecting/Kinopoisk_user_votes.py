import requests
from bs4 import BeautifulSoup
import csv
from time import sleep


login = 'hV5xN2'
password = 'eSMCU3'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0 "
}

proxies = {
    "https": f'http://{login}:{password}@217.29.53.133:12915'
}

def check(name):
    if "сериал" in name:
        return True
    else:
        return False


def parser(user_id,start_pos, proxy):
    count = 0
    with open(f"C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/Users/User_Alex.csv", "a", encoding="utf-8",newline='') as file:
        a_pen = csv.writer(file)
        while True:
            count += 1
            rq = f"https://www.kinopoisk.ru/user/{user_id}/votes/list/ord/date/perpage/200/page/{start_pos+count}/#list"
            response = requests.get(rq, headers=headers, proxies=proxies)
            sleep(10)
            if response.status_code == 404:
                break
            else:
                print('Зашел в else')
                soup = BeautifulSoup(response.text, "lxml")
                if soup.find("html")["prefix"] == "og: http://ogp.me/ns#":
                    print('Найдена Капча')
                    return start_pos+count
                buf = soup.find_all("div", class_="item")
                for i in buf:
                    name = i.find("div", class_="info").find("div", class_="nameRus").find("a").string
                    vote = i.find("div", class_="vote").string
                    id = i.find("div", class_="info").find("div", class_="nameRus").find("a")["href"][6:-1]
                    if check(name):
                        continue
                    else:
                        name = name[:-7]
                        a_pen.writerow((id, name, vote))
        return 'success'

proxies_list = [{
    "https": f'http://{login}:{password}@217.29.53.133:12921'
},
{
    "https": f'http://{login}:{password}@217.29.53.133:12920'
},
{
    "https": f'http://{login}:{password}@217.29.53.133:12919'
},
{
    "https": f'http://{login}:{password}@217.29.53.133:12918'
},
    {
        "https": f'http://{login}:{password}@217.29.53.133:12917'
    },

    {
        "https": f'http://{login}:{password}@217.29.53.133:12916'
    },

    {
        "https": f'http://{login}:{password}@217.29.53.133:12915'
    },
    {
        "https": f'http://{login}:{password}@217.29.53.133:12914'
    },
{
    "https": f'http://{login}:{password}@217.29.53.133:12913'
},
{
    "https": f'http://{login}:{password}@217.29.53.133:12912'
},
]


def main():
    rez = 0
    count = 0
    with open(f"C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/Users/User_Jora.csv", "w", encoding="utf-8",newline='') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(("KP_id","film_name","vote"))
    while True:
        rez = parser(user_id=2063724,start_pos=rez,proxy=proxies_list[count])
        if rez == 'success':
            break
        else:
            if count == 10:
                break
            else:
                count += 1


if __name__ == "__main__":
    main()
