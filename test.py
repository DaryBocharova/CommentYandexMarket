import requests
import csv
from bs4 import BeautifulSoup

def get_html(url,params):
    try:
        result = requests.get(url,params)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_mobile_all():   
    mobile_all=[]    
    links=[]      
    for i in range(1,2): 

        url="https://market.yandex.ru/catalog--mobilnye-telefony/54726/list"
        params = {
        "hid": "91491", 
        "track": "pieces",   
        "onstock": 1,
        "local-offers-first": 0,
        "how": "opinions",
        "page": i
        }

        html = get_html(url,params=params)
        if html:
            soup = BeautifulSoup(html, 'html.parser')     
            #with open("python-org-news.html", "w",encoding="utf8") as f:
            #    f.write(html)   

            all_mobiles = soup.findAll('div', class_='n-snippet-cell2 i-bem b-zone b-spy-visible n-snippet-cell2_type_product')
            
            for all_mobile in all_mobiles:
                link = all_mobile.find('a',class_='n-snippet-cell2__image link').get('href')
                #a=link.find('/',2)
                #b=link[a+1:50]
                link_mobile = link.split('/')
                telefony = link_mobile[2]
                id_telefony = telefony.split('=')
                link_id_telefony = id_telefony[0]
                modile_id = link_id_telefony.split('?')

                if modile_id[0] not in links:
                
                    links.append({
                                "id":modile_id[0]                        

                            }) 


    print(links)


result_review=get_mobile_all()

    