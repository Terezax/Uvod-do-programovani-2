import math

#V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

class Locality:
  def __init__(self, name: str, locality_coefficient: float):
    self.name = name
    self.locality_coefficient = locality_coefficient

  def __str__(self):
    return f"{self.name}, koeficient: {self.locality_coefficient}."

#Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).

class Property:
  def __init__(self, locality: Locality):
    self.locality = locality

  def __str__(self):
    return f"Nemovitost v lokalite {self.locality}"

kocourkov = Locality("Chlupacov", 2.5)
#print(kocourkov)

#Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). 

class Estate(Property):
  def __init__(self, locality, estate_type: str, area: float):
    super().__init__(locality)
    self.estate_type = estate_type
    self.area = area

  def __str__(self):
    return f"{super().__str__()} typu {self.estate_type} a rozlohy {self.area} bude vyse dane KC."
  
  def calculate_tax(self):
    type_coefficients = {
      "land": 0.85,
      "building site": 9,
      "forrest": 0.35,
      "garden": 2
    }
    coefficient = type_coefficients.get(self.estate_type, 1)  # Default to 1 if type not found
    if coefficient is None:
      raise ValueError(f"Neplatny typ pozemku: {self.estate_type}")  
    
    # Vypocet dane z nemovitosti
    sazba_dane = self.area * coefficient * self.locality.locality_coefficient
    return math.ceil(sazba_dane)


kocourkov_2 = Estate(kocourkov, "building site", 600)
print(f"Dan z nemovitosti cini {(kocourkov_2.calculate_tax())}Kc") 

class Residence(Property):
  def __init__(self, locality: Locality, area:float, commercial: bool):
    super().__init__(locality)
    self.area = area
    self.commercial = commercial

  def __str__(self):
    return f"{super().__str__()}, Pozemek v lokalite {self.locality}, o plose {self.area} m2. Je komercni? {self.commercial}"
  
  def calculate_tax(self):
    sazba_dane2 = (self.area * self.locality.locality_coefficient) * 15
    if self.commercial:
      return sazba_dane2 * 2
    else:
      return(sazba_dane2)
    
manetin = Locality("Manetin", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, "land", 900)
print(F"Dan pro zemedelsky pozemek se rovna {zemedelsky_pozemek.calculate_tax()} Kc.")

dum = Residence(manetin, 120, False)
print(f"Dan pro dum se rovna {dum.calculate_tax()} Kc.")

kancelar = Residence(brno, 90, True)
print(F"Dan za kancelar se rovna {kancelar.calculate_tax()} Kc.")

#hotove zakladni zadani
#hotove zakladni zadani
