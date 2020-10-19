import requests
from bs4 import BeautifulSoup

def get_soup_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

def extract_beer_infos(url):
    # Example url: https://www.beerwulf.com/fr-fr/p/bieres/brouwerij-t-verzet-super-noah.33
    soup = get_soup_from_url(url)
    
    # Extract name:
    name = soup.find("h1").text
    
    # Extract evaluation:
    note = soup.find('div', class_='stars')
    note = int(note.attrs['data-percent'])
    
    # Extract price:
    price = soup.select('span.price')[0].text
    price = float(price[:-2].replace(',', '.', 1))  # "2,29 €" => 2.29
    
    # Extract volume:
    volume = soup.find('dt', text='Contenu').find_next_sibling()
    volume = int(volume.text[:-3])  # "33 cl" => 33
    
    infos = {
        'name': name,  # h1, text
        'note': note,  # div, class: stars
        'price': price,  # span, class: price
        'volume': volume,  # dt, text: Contenu
    }
    return infos
