from requests_html import HTMLSession
from lxml import html
import json
import time

class Reviews:
    def __init__(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
        self.url = f'https://www.amazon.in/Apple-iPhone-13-128GB-Blue/product-reviews/{self.asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1'

    def pagination(self, page):
        r = self.session.get(self.url + '&pageNumber=' + str(page))
        r.html.render(sleep=2)
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')
        
    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first=True).text
            rating = review.find('i[data-hook=review-star-rating]', first=True).text
            body_html = review.find('span[data-hook=review-body] span', first=True).html


            if body_html:

                body = html.fromstring(body_html).text_content().replace('\n', '').strip()
            else:
                body = ""

            data = {
                'title': title,
                'rating': rating,
                'body': body[:3000]
            }
            total.append(data)
        return total
    
    def save(self,results):
        with open(self.asin+'-reviews.json','w') as f:
            json.dump(results,f)

if __name__ == '__main__':
    amz = Reviews('B09G9BL5CP')
    results = []


    for x in range(1,300):
        print('Getting Page',x)
        time.sleep(0.5)
        reviews = amz.pagination(x)
        if reviews is not False:
            results.append(amz.parse(reviews))
        else:
            print("No more pages")
    amz.save(results)

