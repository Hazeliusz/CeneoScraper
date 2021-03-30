import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/91715703#tab=reviews")

page_dom = BeautifulSoup(response.text, 'html.parser')

opinion = page_dom.select("div.user-post__card")[0]

opinion_id = opinion["data-entry-id"]
author = opinion.select("span.user-post__author-name")[0].text.strip()
recommendation = opinion.select("span.user-post__author-recomendation > em")[0].text.strip()
stars = opinion.select("span.user-post__score-count")[0].text.strip()
content = opinion.select("div.user-post__text")[0].text.strip()
pros = opinion.select("div.review-feature__col:has(> div[class*='positives']) > div.review-feature__item")[0].text.strip()
cons = opinion.select("div.review-feature__col:has(> div[class*='negatives']) > div.review-feature__item")[0].text.strip()
verified = opinion.select("div.review-pz")[0].text.strip()
post_date = opinion.select("span.user-post_published > time:nth-child(1)['datetime']")[0]["datetime"].strip()
purchase_date = opinion.select("span.user-post_published > time:nth-child(2)['datetime']")[0]["datetime"].strip()
usefulness = opinion.select("button.vote-yes['data-total-vote']")[0].text.strip()
uselessness = opinion.select("button.vote-no['data-total-vote']")[0].text.strip()
print(opinion_id, author, recommendation, stars, content, pros, cons, verified, post_date,
 purchase_date, usefulness, uselessness, sep="\n")

# print(opinion.prettify())
# print(type(opinion))
