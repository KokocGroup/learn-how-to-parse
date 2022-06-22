from os.path import basename

from lib import get_page_content, extract_gtm, get_links, get_scheme_domain_url
import sys


if __name__ == '__main__':

    if len(sys.argv) != 3:
        script_name = basename(sys.argv[0])
        print(f'Пример использования: {script_name} START_PAGE_URL MAX_LEVEL')
        exit(1)

    schema, domain, main_url = get_scheme_domain_url(sys.argv[1])
    if schema not in ['http', 'https'] or not domain:
        print(f'START_PAGE_URL должен быть вида http(s)://site.ru/')
        exit(1)

    max_level = int(sys.argv[2])

    main_url = '/'
    gtms = {}

    current_level = 1
    next_level_urls = {main_url}
    seen_urls = set()

    level = 1
    while level <= max_level:
        print(f'--- level: {level}')
        urls_to_download = next_level_urls - seen_urls
        next_level_urls = set()
        for url in urls_to_download:
            print(f'downloading {url}')
            seen_urls.add(url)
            page_content = get_page_content(f'{schema}://{domain}{url}')
            if not page_content:
                continue
            gtms[url] = extract_gtm(page_content)
            next_level_urls |= get_links(page_content, domain, url)
        level += 1

    main_gtm = gtms[main_url]
    print(f'GTM на главной странице: {main_gtm}')

    for url, gtm in gtms.items():
        if gtm != main_gtm:
            print(f'{gtm} - {url}')
