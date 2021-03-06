from lib import get_page_content, extract_gtm, get_links
import sys


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Передайте первым параметром URL главной страницы')
        exit(1)

    main_url = sys.argv[1]
    page_content = get_page_content(main_url)
    main_gtm = extract_gtm(page_content)
    if main_gtm is None:
        print('GTM не найдена на главной странице')
        exit(1)

    print('На главной странице найдена метка:', main_gtm)
    downloaded_urls = set()
    urls_to_download = get_links(page_content, main_url)

    gtm_same = []
    gtm_differ = []

    cnt = 0
    while(urls_to_download):
        url = list(urls_to_download)[0]
        urls_to_download.remove(url)
        downloaded_urls.add(url)

        page_content = get_page_content(main_url+url)
        gtm = extract_gtm(page_content)
        if gtm == main_gtm:
            gtm_same.append(url)
        else:
            gtm_differ.append(url)
        cnt += 1
        new_links = get_links(page_content, main_url+url)

        urls_to_download |= new_links - downloaded_urls

    print(f'На {len(gtm_differ)} страницах GTM отличается от главной страницы')
    for url in gtm_differ:
        print(url)
