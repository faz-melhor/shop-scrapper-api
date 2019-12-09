import requests
from bs4 import BeautifulSoup

url = 'https://www.hardmob.com.br/forums/407-Promocoes'
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
threads = soup.find_all(class_='threadtitle')

all_threads = []
for thread in soup.find_all(class_='threadtitle'):
    thread_details = dict()
    thread_details['name'] = thread.get_text()
    if thread.find(class_='title'):
        thread_details['link'] = thread.find(class_='title').get('href')
    all_threads.append(thread_details)

print(all_threads)
