names = ["Sampada", "Krunal", "Poha"]
pets = ["Bagheera", "Sheba", "Archie"]

for name_pet in zip(names, pets):
    print(name_pet)

print(dict(zip(names, pets)))

print(type(zip(names, pets)))
