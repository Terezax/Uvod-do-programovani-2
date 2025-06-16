from faker import Faker

fake = Faker('cs_CZ')

for _ in range(10):
  print(fake.name_female())
  
  
for _ in range(10):
    print(fake.address())

