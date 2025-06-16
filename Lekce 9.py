import json

hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open("hours.json", "w", encoding="utf-8") as file:
  json.dump(hours,file, indent=4)
