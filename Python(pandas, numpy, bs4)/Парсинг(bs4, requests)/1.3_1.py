import requests as req
from bs4 import BeautifulSoup
import time
import random
import json

data = {
    'data':[]
}

for page in range(0, 40):
    url = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+разработчик&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}&hhtmFrom=vacancy_search_list"
    headers = {'User-Agent': 'Mozilla/5.0', 'Host': 'rostov.hh.ru'}
    resp = req.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'lxml')
    tags = soup.find_all(attrs={'data-qa': 'serp-item__title'})
    for iter in tags:
        title = iter.text
        resp_object = req.get(iter['href'], headers=headers)
        soup_object = BeautifulSoup(resp_object.text, 'lxml')
        work_experience = soup_object.find(attrs={"data-qa": "vacancy-experience"}).text
        salary = soup_object.find(attrs={"data-qa": "vacancy-salary"}).span.text
        if soup_object.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}) != None:
            region = soup_object.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
        else:
            region = ''
        data['data'].append({"title": title, "work experience": work_experience, 'salary': salary, 'region': region})
        with open('data.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)
        time.sleep(random.randint(1, 3))