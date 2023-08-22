word = "Morning"

vowels = {"a","e","i","o","u"}
vowel_count =0
c_count=0

for ch in word:
    if ch in vowels:
        vowel_count+=1
    else:
         c_count+=1
    print("number of vowels", vowel_count)
    print("number of consenant vowels", c_count)
print(vowel_count)






