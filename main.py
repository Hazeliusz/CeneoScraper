import requests
import re
import json
from bs4 import BeautifulSoup

def get_component(opinion, selector, attribute=None, return_list=False):
    try:
        if attribute:
            return opinion.select(selector)[0][attribute].strip()
        if return_list:
            return [item.get_text().strip() for item in opinion.select(selector)]
        return opinion.select(selector)[0].text.strip()
    except IndexError:
        return None

selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div[class*='positives']) > div.review-feature__item", None, True],
    "cons": ["div.review-feature__col:has(> div[class*='negatives']) > div.review-feature__item", None, True],
    "verified": ["div.review-pz"],
    "post_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "usefulness": ["span[id^='votes-yes']"],
    "uselessness": ["span[id^='votes-no']"]
    }

all_opinions = []
page = 1
product_id = input("Enter product ID: ")

while True:
    response = requests.get(f"https://www.ceneo.pl/{product_id}/opinie-{page}", allow_redirects=False)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            single_opinion = {
                key:get_component(opinion, *value)
                for key, value in selectors.items()
            }
            single_opinion["usefulness"] = int(single_opinion["usefulness"])
            single_opinion["uselessness"] = int(single_opinion["uselessness"])
            single_opinion["content"] = re.sub("\\s", " ", single_opinion["content"])
            single_opinion["stars"] = float(single_opinion["stars"].split("/")[0].replace(",", "."))
            single_opinion["recommendation"] = True if single_opinion["recommendation"] == "Polcam" else False if single_opinion["recommendation"] == "Nie polecam" else None
            single_opinion["verified"] = bool(single_opinion["verified"])
            all_opinions.append(single_opinion)
        page += 1
    else: break

with open(f"./opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, ensure_ascii=False, indent=4)
