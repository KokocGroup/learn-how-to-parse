from lib import get_page_content, extract_gtm, get_links
import sys


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Передайте первым параметром URL главной страницы')

    main_url = sys.argv[1]
    page_content = get_page_content(main_url)
    main_gtm = extract_gtm(page_content)
    if main_gtm is None:
        print('GTM не найдена на главной странице')
        exit(1)

    print(main_gtm)
    uniq_urls = get_links(page_content, main_url)

    print(f'найдено {len(uniq_urls)} уникальных ссылок')
    cnt = 0
    for url in uniq_urls:
        page_content = get_page_content(main_url+url)
        gtm = extract_gtm(page_content)
        print(gtm == main_gtm, url)

        cnt += 1

        if cnt > 5:
            break
