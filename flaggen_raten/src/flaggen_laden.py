import json
import os
import requests

datei = open("laender.json", encoding="utf-8") 
laender = json.load(datei)

for land in laender: 
    datei_name = land["cca3"]
    #hauptstadt = land["capital"]
    flagge_url = land["flags"]["png"]
    print(datei_name)
    #print(hauptstadt)
    print(flagge_url)

    response = requests.get(flagge_url)
    if response.status_code == 200:
        with open(os.path.join("src","assets", (datei_name + ".png")), "wb") as file:
            file.write(response.content)   
            print("Flagge von " + datei_name + " wurde erfolgreich heruntergeladen.")        

datei.close()