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
  #print(data) # to explore
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

headers_subjekty = {
  "accept": "application/json",
  "Content-Type": "application/json",
}

data_subjekty = {"obchodniJmeno": (nazev_subjektu)}
response_subjekty = requests.post(url, headers=headers_subjekty, json=data_subjekty)

ciselnik = ("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat")

headers_ciselnik = {
  "accept": "application/json",
  "Content-Type": "application/json",
}

data_ciselnik = {"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}
response_ciselnik = requests.post(ciselnik, headers=headers_ciselnik, json=data_ciselnik)

ciselnik_data = response_ciselnik.json()
polozky = ciselnik_data['ciselniky'][0]["polozkyCiselniku"]

print(json.dumps(response.json(), indent=2, ensure_ascii=False))

def find_legal_form(kod, polozky):
  for polozka in polozky:
    if polozka["kod"] == kod:
      nazvy = polozka.get("nazev", [])
      if nazvy and isinstance(nazvy, list):
        return nazvy[0].get("nazev", "Neznama pravni forma")
      return "Neznama pravni forma"
  return "Neznama pravni forma"

#checking valid response, converting response to JSON, looking for "ekonomickeSubjekty"
if response_subjekty.status_code == 200:
    vysledky = response_subjekty.json()  
    pocet = vysledky.get("pocetCelkem", 0)
    subjekty = vysledky.get("ekonomickeSubjekty", [])

    if pocet == 0 or not subjekty:
      print("Nebyl nalezen zadny subjekt")
    else:
      print(f"Nalezeno subjektu: {pocet}")
      for item in subjekty:
        obchodni_jmeno = item.get('obchodniJmeno', 'NeznameJmeno')
        ico = item.get('ico', 'Nezname ICO')
        kod_pravni_formy = item.get('pravniForma')

        pravni_forma_nazev = find_legal_form(kod_pravni_formy, polozky)
        
        print(f"{obchodni_jmeno}, {ico}, {pravni_forma_nazev}")       
else:
  print('Chyba pri vyhledavani subjektu')

