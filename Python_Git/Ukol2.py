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
  #getting required key values
  obchodni_jmeno = data.get("obchodniJmeno", "Nazev neexistuje")
  sidlo = data.get('sidlo', {})
  textova_adresa = sidlo.get('textovaAdresa', 'Adresa neexistuje')

  print(obchodni_jmeno)
  print(textova_adresa)
else:
  print(f"Chyba, ICO nenalezeno.")
  exit()

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
  pocet = vysledky.get("pocetCelkem", 0)
  subjekty = vysledky.get("ekonomickeSubjekty")

  if pocet == 0 or not subjekty:
    print("Nebyl nalezen zadny subjekt")
  else:
    print(f"Nalezeno subjektu: {pocet}")

  for item in subjekty:
    print(f"{item.get('obchodniJmeno', 'Nezname jmeno')}, {item.get('ico', 'nezname ico')}")
else:
  print('Chyba pri vyhledavani subjektu')

