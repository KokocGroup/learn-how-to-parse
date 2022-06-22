import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def get_page_content(url):
    request = requests.get(url)
    if request.status_code == 200:
        return request.text


def extract_gtm(page_content):
    match = re.search(r"Google Tag Manager -->(.*?'(GTM-[0-9a-zA-Z]+)'.*?)<!-- End Google Tag Manager", page_content, re.DOTALL)
    if match is not None:
        return match.group(2)


def get_scheme_domain_url(url):
    url_parts = urlparse(url)
    return url_parts.scheme, url_parts.netloc, url_parts.path


def get_links(page_content, domain, base_url):
    uniq_urls = set()
    soup = BeautifulSoup(page_content, "html.parser")
    for link in soup.findAll('a'):
        url = link.get('href')
        url_parts = urlparse(url)
        if url_parts.scheme not in ['', 'http', 'https']:
            continue
        if url_parts.netloc not in ['', domain]:
            continue

        if url_parts.path.startswith('/'):
            clean_url = f'{url_parts.path}'
        else:  # обрабатываем случай относительных URL'ов
            if base_url.endswith('/'):
                base_url = base_url[:-1]
            clean_url = f'{base_url}/{url_parts.path}'

        if url_parts.query:
            clean_url = f'{clean_url}?{url_parts.query}'

        uniq_urls.add(clean_url)
    return uniq_urls
