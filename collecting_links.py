from bs4 import BeautifulSoup
import requests
import time,random


headers = {
    "Accept": "*/*",
    "user-agent": " "
}

def item_name(name,price):
    with open(f"name_item.html",'a', encoding='utf-8') as file:
        file.write(name.text + ' | ' +  price + '\n')
    


def urls(headers, url):
    
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
            
        html = r.json()['results_html']
        
        soup = BeautifulSoup(html, "lxml")
        
        name_item = soup.find_all('a', class_='market_listing_row_link') 
        
        
        
        for el in name_item:
            item_url = el.get('href') 
            name = el.find('span', class_='market_listing_item_name')
            
            price = el.find('span', class_='sale_price').text 
            
            if price >= min_price and price <= max_price:    
                
                name = el.find('span', class_='market_listing_item_name')
                
                with open(f"url.html",'a', encoding='utf-8') as file:
                    file.write( item_url + '\n') 
                
                item_name(name,price)
            time.sleep(2)


    else:
        print('\n' + 'Подождите немного' + '\n')
        time.sleep(40)
        urls(headers, url)


start = int(input('С какой страницы '))
start = (start - 1)* 10           
number_str = 1 
n = int(input('Введите количество страниц: '))
min_price = input('Введите минимальную цену в USD: ')
min_price = '$' + str(min_price) + ' USD'
max_price = input('Введите максимальную цену в USD: ')
max_price = '$' + str(max_price) + ' USD'


slots = ['tag_armor', 'tag_weapon', 'tag_head', 'tag_offhand_weapon', 'tag_mount', 'tag_legs', 'tag_shoulder', 'tag_belt', 'tag_arms'] # 'tag_back', 'tag_tail','tag_neck'

for slot in slots:
    for st in range(n):
        st += 1
        url = f'https://steamcommunity.com/market/search/render/?query=&start={start}&count=10&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=570&category_570_Slot[]={slot}&category_570_Quality[]=tag_strange'

        urls(headers=headers, url=url)
        
        start += 10
        print(str(number_str) + ' страница готова! ')
        
        time.sleep(random.randint(1,2))
        
        number_str += 1
        
    with open(f"url.html",'a', encoding='utf-8') as file:
            file.write('\n' + '-' * 50 + '\n')
    with open(f"name_item.html",'a', encoding='utf-8') as file:
        file.write('\n' + '-' * 50 + '\n')

