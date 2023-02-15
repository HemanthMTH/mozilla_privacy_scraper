class Product(object):
    product_name = ''
    manufacturer_name = ''
    manufacturer_url = ''
    product_url = ''
    date_of_analysis = ''
    time_spent_on_research = ''
    mozilla_rating = ''
    people_rating = ''

    def __init__(self, product_name, manufacturer_name, manufacturer_url, product_url, date_of_analysis, time_spent_on_research, mozilla_rating, people_rating):
        self.product_name = product_name
        self.manufacturer_name = manufacturer_name
        self.manufacturer_url = manufacturer_url
        self.product_url = product_url
        self.date_of_analysis = date_of_analysis
        self.time_spent_on_research = time_spent_on_research
        self.mozilla_rating = mozilla_rating
        self.people_rating = people_rating




