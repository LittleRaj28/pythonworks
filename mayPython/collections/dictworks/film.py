movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}
wc={}

#print all movie names
print(movies.keys())


#top rated movies
print(max(movies,key=lambda k:movies.get(k)))


#sort movies wrt rating order by desc
out=sorted(movies,key=lambda k:movies.get(k),reverse=True)
print(out)

