from bs4 import BeautifulSoup
import requests
import time

headers = {
    "Accept": "*/*",
    "user-agent": " "
}

def comparison(url,name,price):
    
        
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
    
        with open(f"html_items.html",'w', encoding='utf-8') as file:
            file.write(r.text)
        with open(f"html_items.html", encoding='utf-8') as file:
            src = file.read()
            
        soup = BeautifulSoup(src, "lxml")

        html_item = soup.find_all('a', class_='market_listing_row_link')
        
        for el in html_item:
            list_item = el.find('span', class_='market_listing_item_name')
            price_item = el.find('span', class_='sale_price').text
            
            for name_item in list_item:
                if name == name_item: 
                    if price_item > price:
                        with open(f"list_item.html",'a', encoding='utf-8') as file:
                            file.write(name + '\n')
                        print(name + ' подходит под критерии')
                    else:
                        print('Цена ' + name + ' не подходит')
                    
                
            time.sleep(0.5)
    else:
        print('\n' + 'Подождите немного' + '\n')
        time.sleep(40)
        comparison(url, name, price)



with open(f"name_item.html", encoding='utf-8') as file:
    lists = file.readlines()

pr = '-' * 50 + '\n'


for item in lists:
    if item != '\n' and item != pr:
        name = item.replace('Inscribed ','').partition(' |')[0].replace(' ', '_')
        price = item.partition('| ')[2].replace('\n', '')
        
        
        url = 'https://steamcommunity.com/market/search?category_570_Hero%5B%5D=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category_570_Quality[]=tag_unique&appid=570&q=' + name
        
        name = name.replace('_',' ')
        comparison(url,name,price)
        
        time.sleep(1)


