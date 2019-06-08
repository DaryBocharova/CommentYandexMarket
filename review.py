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


def get_python_news():   
    result_review=[]
    for i in range(1,70):            
        
        url="https://market.yandex.ru/product--smartfon-xiaomi-redmi-4-prime/1713398799/reviews"
        params = {
        "hid": "91491",
        "page": i        
        }

        print(params)
        html = get_html(url,params=params)

        if html:
            soup = BeautifulSoup(html, 'html.parser')        
            all_review = soup.findAll('dl', class_='n-product-review-item__stat')
           


            for review in all_review:
                try:

                    title=review.find('dt',class_='n-product-review-item__title').text
                    text_review=review.find('dd',class_='n-product-review-item__text').text         

                    result_review.append({
                        "title":title,
                        "text_review": text_review    

                    }) 
                    
                except:
                    next 
    
    return result_review
            
        
         
result_review=get_python_news()
with open('review.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['title', 'text_review']
    writer = csv.DictWriter(f, fields)
    writer.writeheader()
    for user in result_review:
        writer.writerow(user)