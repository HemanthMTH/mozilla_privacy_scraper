
from bs4 import BeautifulSoup

import os
import json
from product import Product
import time


def process_record(product: Product):
    new_prod = {
        "product_name": product.product_name,
        "manufacturer_name": product.manufacturer_name,
        "manufacturer_url": product.manufacturer_url,
        "product_url": product.product_url,
        "date_of_analysis": product.date_of_analysis,
        "time_spent_on_research": product.time_spent_on_research,
        "mozilla_rating": product.mozilla_rating,
        "people_rating": product.people_rating,
    }

    return new_prod


products = []

def parse(scraper, dir):
    print('Started parsing product pages')
    start = time.time()
    path = os.path.join(dir, 'product_urls.txt')
    with open(path, 'r') as f:
        for url in f:
            url = url.rstrip()
            req = scraper.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            divs = soup.find_all("div", {"class": "row intro"})
            a = [i.find_all('div', {"class": "col-12",}) for i in divs]
            n = [i.find('h1', {"class": "tw-h1-heading col-12",}) for i in divs]
            p_name = n[0].get_text()
            b = [i.find('a', {"class": "company-external-link",}) for i in a[0]]
            man_url = b[0]['href']
            man_name = b[0].get_text()
            c = [i.find('p', {"class": "tw-body-small date-reviewed",}) for i in a[0] if i.find('p', {"class": "tw-body-small date-reviewed",}) is not None]
            f = len('Review date: ')
            review_time = c[0].get_text()[f:]
            d = [i.find('a', {"class": "tw-body-small time-researched",}) for i in a[0] if i.find('a', {"class": "tw-body-small time-researched",}) is not None]
            research_time = d[0].next_sibling.strip()
            e = [i.find('span', {"class": "people-voted",}) for i in a[0] if i.find('span', {"class": "people-voted",}) is not None]
            creepiness = e[0].get_text()
            f = [i.find('p', {"class": "tw-body-small mozilla-says thumb-up",}) for i in a[0] if i.find('p', {"class": "tw-body-small mozilla-says thumb-up",}) is not None]
            g = [i.find('p', {"class": "tw-body-small mozilla-says  thumb-side",}) for i in a[0] if i.find('p', {"class": "tw-body-small mozilla-says  thumb-side",}) is not None]
            feedback = ''
            if len(f) > 0:
                feedback = 'Likes'
            elif len(g) > 0 : 
                feedback = None
            else:
                feedback = 'Dislikes'

            product = Product(p_name, man_name, man_url, url, review_time, research_time, feedback, creepiness)

            products.append(process_record(product))

        with open(os.path.abspath(os.path.join(dir, "product_details.json")), "w") as f:
                json.dump(products, f, indent=2)
        end = time.time()
        print('Done parsing products!!')
        print('Time taken to parse:', end - start)