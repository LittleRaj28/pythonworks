bikes = {"Name":"R15","price":150000,"mileage":55}
# print(bikes)

if("price" in bikes):
    print(bikes["price"])
else:
    print("not present")

 #print all key value pair


for key in bikes:
    print(key,bikes[key])

 #add new key value pair

bikes["year"]=2019
print(bikes)

# add 5000 rs discount

bikes["price"] -= 5000
print(bikes)



