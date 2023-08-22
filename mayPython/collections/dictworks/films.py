movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]

#q1  print all movie names

for m in movies:
    print(m.get("name"))
    #list comprehension

# movie_names = [m.get("name") for m in movies ]

#q2 print  filter movies with genre =mystery

for m in movies:
  if m.get("genres")=="mystery":
      print(m.get("name"))

#list comprehension

mysterys=[m.get("name") for m in movies if "mystery "in m.get("genres")]
print(mysterys)




 #q3 top rated movies
print( max(movies,key = lambda m:m.get("rating")))

#q4 print malayalam movies
mal_movie=[m.get("name")for m in movies if "malayalam" in m.get("language")]
print(mal_movie)

#q5 movie name released in 2023

years=[m.get("name")for m in movies if m.get("year")==2023]
print(years)



#q6 order movies wrt rating order by desc

movies_sorted=sorted(movies,reverse =True,key = lambda m:m.get("rating"))
print(movies_sorted)

