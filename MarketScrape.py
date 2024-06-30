from bs4 import BeautifulSoup
import requests
import time

def find_item():
        
    url = "https://www.facebook.com/marketplace/"
    print("searching your query...")
    time.sleep(3)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    price = soup.find_all('div', class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u")
    vehcile_name = soup.find_all('span', class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
    location = soup.find_all('span', class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84")
    print("Price: ", price)
    print("Vehicle: ", vehcile_name)
    print("Location: ", location)
            
        

find_item()
