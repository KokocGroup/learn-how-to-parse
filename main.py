import requests
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

print(reqeust.text.count('Google Tag Manager'))
