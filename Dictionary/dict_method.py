car = {
    "brand": "Toyota",
    "model": "Innova",
    "year": 2022
}

print(car.keys())      # dict_keys(['brand', 'model', 'year'])
print(car.values())    # dict_values(['Toyota', 'Innova', 2022])
print(car.items())     # dict_items([('brand', 'Toyota'), ('model', 'Innova'), ('year', 2022)])

# Looping using .items() — gets key AND value together, cleaner than before
for key, value in car.items():
    print(key, "->", value)
