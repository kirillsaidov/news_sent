# module download_google_news

import os
import csv
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path


"""
prep
"""

def get_timedelta(delta: str):
    delta_split = delta.lower().replace('live', '').split(' ')
    delta_num = delta_split[0]
    delta_unit = delta_split[1]
    if 'min' in delta_unit:
        return timedelta(minutes=int(delta_num))
    elif 'hour' in delta_unit:
        return timedelta(hours=int(delta_num))
    elif 'day' in delta_unit:
        return timedelta(days=int(delta_num))
    else:
        return timedelta(seconds=int(delta_num))


def days_between(d1: str, d2: str):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


"""
scap news data
"""


# links
google_links = [
    'https://www.google.com/search?q=bitcoin&num=100&sca_esv=600189765&gl=us&tbas=0&tbs=sbd:1&tbm=nws&ei=nSqxZaPZMs3_7_UP5rKLkAQ&start=0&sa=N&ved=2ahUKEwjjm5vEqfaDAxXN_7sIHWbZAkI4ZBDy0wN6BAgEEAQ&biw=1872&bih=978&dpr=1',
    'https://www.google.com/search?q=bitcoin&num=100&sca_esv=600189765&gl=us&tbas=0&tbs=sbd:1&tbm=nws&ei=eNWsZaraE4C79u8P2PmHgAM&start=100&sa=N&ved=2ahUKEwiq9qzih-6DAxWAnf0HHdj8ATAQ8tMDegQIARAE&biw=941&bih=978&dpr=1',
    'https://www.google.com/search?q=bitcoin&num=100&sca_esv=600189765&gl=us&tbas=0&tbs=sbd:1&tbm=nws&ei=eNWsZaraE4C79u8P2PmHgAM&start=200&sa=N&ved=2ahUKEwiq9qzih-6DAxWAnf0HHdj8ATAQ8tMDegQIARAE&biw=941&bih=978&dpr=1',
    'https://www.google.com/search?q=bitcoin&num=100&sca_esv=600189765&gl=us&tbas=0&tbs=sbd:1&tbm=nws&ei=eNWsZaraE4C79u8P2PmHgAM&start=300&sa=N&ved=2ahUKEwiq9qzih-6DAxWAnf0HHdj8ATAQ8tMDegQIARAE&biw=941&bih=978&dpr=1',
]

# get htmls
google_htmls = []
for link in google_links:
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        google_htmls.append(response.content)
    
# parse htmls
google_news = []
published_today = 0
for html in google_htmls:
    soup = BeautifulSoup(html, 'html.parser')
    for el in soup.select("div.SoaBEf"):
        entry = {
            'title': el.select_one('div.MBeuO').get_text(),
            'source': el.select_one('.NUnG9d span').get_text(),
            'link': el.find('a')['href'],
            'snippet': el.select_one('.GI74Re').get_text(),
            'date': el.select_one('.LfVVr').get_text(),
        }
        
        # corret date
        datetime_now = datetime.now()
        pub_date = datetime_now - get_timedelta(entry['date'])
        entry['date'] = pub_date.strftime("%Y-%m-%d")
        
        # save
        daydiff = abs((datetime_now - pub_date).days)
        if daydiff < 2:
            google_news.append(entry)
                
        # count            
        published_today = published_today + int(pub_date.date() == datetime_now.date())


"""
save and output some stats:
    - num of news
    - num of news today
    - num of news yesterday
"""

# create cache folder
save_folder = './cache/webscrapping'
Path(save_folder).mkdir(parents=True, exist_ok=True)

# save dataset
df = pd.DataFrame(google_news)
df.to_csv(os.path.join(save_folder, f'{datetime.now().strftime("%Y-%m-%d")}.csv'), index=False, quoting=csv.QUOTE_ALL)

print('------------------------------')
print('REPORT:')
print(f' - [ {len(google_news):3d} ] news found')
print(f' - [ {published_today:3d} ] published today')
print(f' - [ {(len(google_news) - published_today):3d} ] published yesterday')
print('------------------------------')


# classify news headlines
# calculate positivity rate: yesterday, today, 2-day overall rate
