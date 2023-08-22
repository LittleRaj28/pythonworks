words = ["hello","good","aabbcccdef","morning"]

print(min(words,key = lambda w:len(w)))    #min

print(max(words,key = lambda w:len(w)))    #max

lst = [2,45,64,234,236]
print(sorted(lst))

print(sorted(lst,reverse=True))



word = ["in","hello","hai","pneumonoultra","good"]

print(sorted(word,reverse=False))

out= print(sorted(words,reverse =True,key = lambda w:len(w)))
print(out)


