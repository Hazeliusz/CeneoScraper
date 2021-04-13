import requests
import re
import json
from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/91715703#tab=reviews")

page_dom = BeautifulSoup(response.text, 'html.parser')

all_opinions = []

opinions = page_dom.select("div.user-post__card")
for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.select("span.user-post__author-name")[0].text.strip()
    try:
        recommendation = opinion.select("span.user-post__author-recomendation > em")[0].text.strip()
        recommendation = True if recommendation=="Polecam" else False
    except IndexError:
        recommendation = None
    stars = opinion.select("span.user-post__score-count")[0].text.strip()
    stars = float(stars.split("/")[0].replace(",", "."))
    content = opinion.select("div.user-post__text")[0].text.strip()
    content = re.sub("\\s", " ", content)
    pros = opinion.select("div.review-feature__col:has(> div[class*='positives']) > div.review-feature__item")
    pros = [item.get_text().strip() for item in pros]
    cons = opinion.select("div.review-feature__col:has(> div[class*='negatives']) > div.review-feature__item")
    cons = [item.get_text().strip() for item in cons]
    try:
        verified = bool(opinion.select("div.review-pz")[0].text.strip())
    except IndexError:
        verified = False
    try:
        post_date = opinion.select("span.user-post_published > time:nth-child(1)")[0]["datetime"].strip()
    except IndexError:
        post_date = None
    try:
        purchase_date = opinion.select("span.user-post_published > time:nth-child(2)")[0]["datetime"].strip()
    except IndexError:
        purchase_date = None
    usefulness = int(opinion.select("span[id^='votes-yes']")[0].text.strip())
    uselessness = int(opinion.select("span[id^='votes-no']")[0].text.strip())

    single_opinion = {
        "opinion_id": opinion_id,
        "author": author,
        "recommendation": recommendation,
        "stars": stars,
        "content": content,
        "pros": pros,
        "cons": cons,
        "verified": verified,
        "post_date": post_date,
        "purchase_date": purchase_date,
        "usefulness": usefulness,
        "uselessness": uselessness
    }


    all_opinions.append(single_opinion)
    
print(json.dumps(all_opinions, ensure_ascii=False))

# print(opinion.prettify())
# print(type(opinion))
