import requests
from bs4 import BeautifulSoup as BS

#r = requests.get("https://parad.by/products")
#html = BS(r.content, 'html.parser')

URL = "https://parad.by/products" # адрес по которому будет проходить парсинг

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 'Accept': '* / *'}
# параметры HEADERS User-Agent и Accept нужно переадать, что бы браузер воспринимал нас как человека а не робота
# берем их во вкладке разработчика СЕТЬ и открываем первый документ
HOST = "https://parad.by/" # создаем начало ссылки, что бы получилась правильная ссылка с полным адресом

# функция get_html принимает URL страницы которую мы рассматриваем и params если нужно будет передавать дополнительные страницы к url
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params) #запрос запрос на получение объекта данных
    return r



# эта функции будет распарсивать то что получно в parce()
def get_content(html):
    soop = BS(html, 'html.parser') # передаем в переменную soop полученную информацию через библиотеку BS
    items = soop.find_all('div', class_='user_product_data_col') # получем всю информацию из soop и передаем ее в items
    #print(items)

    materials = []
    for item in items:
        materials.append({
            'title': item.find('h6').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
        })
    print(materials)
    #print(len(materials))

def parse():
    html = get_html(URL) # в переменную html записываем данные которые передадуться при вызове ф-ии get_html с нужным URL
    if html.status_code == 200: # проверка что мы достучались до сервера и его ответ 200 т.е. все ОК
        get_content(html.text)
        #print(html.text) # печатаем исходный код страницы который нам нужно теперь распарсить при помощи ф-иии get_content
        #print(html.content)  # печатаем исходный код страницы в закодированном виде
    else:
        print('Error') # в противном случае возващаем ошибку

parse()


# for el in html.select(".user_product_special_border"):
#     title = el.select("strong")
#     print(title[0].text)





