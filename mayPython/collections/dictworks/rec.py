text = "ABBAACDA"
# MOST RECURSIVE CHARACTER

wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
        print(wc)

#most recursive

print(max(wc,key=lambda k:wc.get(k)))

