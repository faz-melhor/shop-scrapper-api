import requests
from bs4 import BeautifulSoup, UnicodeDammit


def scrap_hardmob():
    url = 'https://www.hardmob.com.br/forums/407-Promocoes'
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')
    threads = soup.find_all(class_='threadtitle')

    all_threads = []
    for thread in soup.find_all(class_='threadtitle'):
        thread_details = dict()
        decoded_string = UnicodeDammit(thread.text.strip())
        thread_details['title'] = decoded_string.unicode_markup
        if thread.find(class_='title'):
            thread_details['link'] = thread.find(class_='title').get('href')
        all_threads.append(thread_details)

    # Removed first headers
    return all_threads[3::]
