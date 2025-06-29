#PART 1
#import required libraries
import json
import requests

#asking user to insert required ICO, validating input meeting the official ICO requirements
ico = input("Prosim, vlozte pozadovane ICO: ")

if not ico.isdigit() or len(ico) != 8:
  print("Vlozte platne ICO. Musi mit presne 8 cislic.")
  exit()

#getting data from ARES
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

#validating response and converting it into JSON
if response.status_code == 200:
  data = response.json()
  print(data) # to explore
else:
  print(f"Chyba, ICO nenalezeno.")

#getting required key values
obchodni_jmeno = data.get("obchodniJmeno", "Nazev neexistuje")
sidlo = data.get('sidlo', {})
textova_adresa = sidlo.get('textovaAdresa', 'Adresa neexistuje')

print(obchodni_jmeno)
print(textova_adresa)

#PART 2
# imports done

nazev_subjektu = input("Vlozte nazev hledaneho subjektu: ")
url = ("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat")

headers = {
  "accept": "application/json",
  "Content-Type": "application/json",
}

data = {"obchodniJmeno": (nazev_subjektu)}
response = requests.post(url, headers=headers, json=data)

#checking valid response, converting response to JSON, looking for "ekonomickeSubjekty"
if response.status_code == 200:
  vysledky = response.json()  
  subjekty = vysledky.get("ekonomickeSubjekty")

  for item in subjekty:
    print(item.get("obchodniJmeno"), item.get("ico"))

#Bonus


