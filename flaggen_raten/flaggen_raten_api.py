import json
import requests

url = "https://restcountries.com/v3.1/all?fields=name,flags,borders,capital,continents,translations,languages,population,cca3"

response = requests.get(url)
print(response)

if response.status_code == 200:
    laender = response.json()

    with open("laender.json", "w", encoding="utf-8") as f:
        json.dump(laender, f, ensure_ascii=False, indent=4)