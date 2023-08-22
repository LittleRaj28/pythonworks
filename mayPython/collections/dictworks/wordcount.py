text = "ABABC"
# find first recursive character

#step1 create empty dictionary

# wc = {}
# for ch in text:
#     if ch in wc:
#         print(ch,"is first  recursive character")
#         break
#     else:
#         wc[ch]=1

# a:2 b:2 c:1
# wc = {}
# for ch in text:
#      if ch in wc:
#          wc[ch]+=1
#      else:
#          wc[ch]=1
#          print(wc)

words = ["hello","hai","hello","hai","good","morning","evening"]
#word count
#{hello:2,hai:2,good:1,morning:1,evening:1}

wc = {}
for ch in words:
     if ch in wc:
         wc[ch]+=1
     else:
         wc[ch]=1
         print(wc)




