word = input("enter a string")
out = input("enter another string")
sort_word = sorted(word)
sort_out = sorted(out)
print(sort_word)
print(sort_out)

print("anagram" if sort_word==sort_out else "not anagram")