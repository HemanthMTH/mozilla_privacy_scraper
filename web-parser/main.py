
from bs4 import BeautifulSoup
import cloudscraper
import os
import product_parser



if __name__ == '__main__':
    
    dir = os.getcwd()
    category_urls_path = os.path.join(dir, 'category_urls.txt') 

    scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
    
    with open(category_urls_path, 'r') as f:
        print('Stared parsing categories to fetch product URLs..')
        for url in f:
            url = url.rstrip()
            req = scraper.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            figs = soup.find_all("figure", {"class": "product-box"})
            current_category_prod_urls = [i.find('a', {"class": "product-image",})['href'] for i in figs]
            with open('product_urls.txt', 'w', encoding="utf-8") as f:
                for prod_url in current_category_prod_urls:
                    f.write("%s\n" % prod_url)

    print("Done fetching URLs!!")

product_parser.parse(scraper, dir)

