from json import load

with open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\restCountries\\restt.json",encoding="UTF-8")as f:
    data=load(f)
    print(len(data))

# print all country names
for c in data:
    print(c.get("name"))


# print all region names

    # print(c.get("region")) #prints repeatedly

all_regions ={c.get("region") for c in data}
print(all_regions)

# print asian country names

asian_country=[c.get("name")for c in data if c.get("region")=="Asia"]

print(asian_country)


# print population of afghanistan

afghan_population = [c.get("name") for c in data if c.get("region")=="Asia"]

print(afghan_population)

#indian borders


country_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
print(country_borders)

country_border_names =[c.get("name") for c in data if c.get("alpha3Code") in country_borders]
print(country_border_names)


# print currency code

#print country with highest population