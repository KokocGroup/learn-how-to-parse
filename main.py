import requests
from bs4 import BeautifulSoup
import re


main_url = 'https://kokoc.com'

request = requests.get(main_url)

# with open('kokoc.html', 'w') as f:
#     f.write(request.text)

# if 'Google Tag Manager' in request.text:
#     print('Google Tag Manager is present')


match = re.search(r"Google Tag Manager -->(.*?'(GTM-[0-9a-zA-Z]+)'.*?)<!-- End Google Tag Manager", request.text, re.DOTALL)
if match is not None:
    print(match.group(1))
    gtm = match.group(2)
else:
    print('ничего не найдено')

# <a class="sdkjfk" href='''...'''>


uniq_urls = set()
soup = BeautifulSoup(request.text, "html.parser")
for link in soup.findAll('a'):
    url = link.get('href')
    if url:
        url = url.split('#')[0]
    if url:
        if main_url in url:
            url = url.replace(main_url, '')
        if url.startswith('http://') or url.startswith('https://') or url.startswith('mailto:'):
            continue
        uniq_urls.add(url)

print(f'найдено {len(uniq_urls)} уникальных ссылок')
cnt = 0
for url in uniq_urls:
    print(url)
    cnt += 1

    if cnt > 5:
        break
