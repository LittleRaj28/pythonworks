from json import load

with open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\movies\\mdb.json","r")as f:
    data = load(f)

    # total number of movies

print(len(data))

# print all movie names

all_movienames =[m.get("title")for m in data]
print(all_movienames)


# print movie with highest runtime

movie_runtime= max(data,key=lambda s:int(s.get("runtime")))
print(movie_runtime.get("title"))


# print all genres

all_genres ={g for m in data for g in m.get("genres")}
print(all_genres)
# print movie name which contain  genres comedy

comedy_genre = [m.get("title") for m in data if "Comedy"in m.get("genres")]
print(comedy_genre)
# print movie name which contain  genres comedy or Fanstasy

genre_filter = {m.get("title")for m in data for g in m.get("genres") if g in ["Comedy","Fantasy"]}
print(genre_filter)

# year wise movie count {1988:5,1984:3}
yc={}
for m in data:
    years=m.get("year")
    if years in yc:
        yc[years]+=1
    else:
        yc[years]=1
print(yc)
print(max(yc,key =lambda k:yc.get(k)))  # similar method of         person= {name:hari}
                                        #                            person.get("name")

print(min(yc,key=lambda y:yc.get(y)))



