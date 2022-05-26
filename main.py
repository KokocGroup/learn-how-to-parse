import requests
import re

url = 'http://kokoc.com/'

reqeust = requests.get(url)

# with open('kokoc.html', 'w') as f:
#     f.write(reqeust.text)

if 'Google Tag Manager' in reqeust.text:
    print('Google Tag Manager is present')


print(reqeust.text.count('Google Tag Manager'))
