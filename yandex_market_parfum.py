import requests
from bs4 import BeautifulSoup
import csv




def get_html(url):
    r = requests.get(url)

    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='n-w-reviews__pager').find_all('a', class_='button_action_yes button button_size_s button_theme_pseudo button_side_right n-pager__button-number i-bem n-smart-link')[-1].text
    
    return int(pages)

def get_pagedata(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='layout__col layout__col_size_p75').find_all('div', class_='n-product-review-item i-bem n-product-review-item_collapsed_yes n-product-review-item_js_inited')

    for ad in ads:
        #pos, neg, comment, rating, url
        try:
            pos = ad.find('dl', class_='n-product-review-item__stat').find_all('dd', class_='n-product-review-item__text').text.strip()
        except:
            pos = ''
        try:
            neg = ad.find('dl', class_='n-product-review-item__stat').find_all('dd', class_='n-product-review-item__text').text.strip()
        except:
            neg = ''
        try:
            comment = ad.find('dl', class_=)

        
def main():
    url = 'https://market.yandex.ru/product--dolce-gabbana-3-l-imperatrice/14282120/reviews?hid=15927546&page=2'
    base_url = 'https://market.yandex.ru/product--dolce-gabbana-3-l-imperatrice/14282120/reviews'
    page_part = 'page='
    query_part = '?hid=15927546&'

    pages = get_total_pages(get_html(url))

    for i in range(1, pages):
        url_gen = base_url +  query_part + page_part + str(i)
        print(url_gen)

        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
     main()