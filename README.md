# CeneoScraper
## Stage 1 - extraction of all components for single opinion
1. extraction of signe web page content
2. analysis of single opinion structure

|Component|CSS selector|Variable name|Data type|
|---------|------------|-------------|---------|
|Opinion|div.user-post__card|opinion|dict|
|Opinion id|["data-entry-id"]|opinion_id|str|
|Author|span.user-post__author-name|author|str|
|Recommendation|span.user-post__author-recomendation > em|recommendation|bool|
|Star rating|span.user-post__score-count|stars|float|
|Content|div.user-post__text|content|str|
|Adventages|div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item|pros|list(str)|
|Disadventages|div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item|cons|list(str)|
|Verification|div.review-pz|verified|bool|
|Post date|span.user-post_published > time:nth-child(1)["datetime"]|post_date|str|
|Purchase date|span.user-post_published > time:nth-child(2)["datetime"]|purchase_date|str|
|Usefulness count|span[id^='votes-yes']|useful|int|
|Uselessness count|span[id^='votes-no']|useless|int|

3. extraction of single opinion components
4. transformation of extracted data to given data types

## Stage 2 - extraction of all opinions from single page
1. definition of dictionary to store all components of single opinion
2. definition of list for opinions dictionaries storing
3. implementation of loop traversing through all opinions from single page

## Stage 3 - extraction of all opinions for single product
1. implementation of loop traversing through consectuive pages with opinions
2. loading extracted opinions to .json file
3. parametrization 

## Stage 4 - refactoring