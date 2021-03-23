import requests

response = requests.get("https://www.ceneo.pl/91715703#tab=reviews")
print(response.text)