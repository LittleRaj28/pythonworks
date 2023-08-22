# word="hello"
# print(word.capitalize()) #to capitalize the first character
# #casefold() to lowercase the given string
# print(word.casefold())
# #count(ch) count of the specified character
# print(word.count("l"))
# #split(separator) to split into a list using the separator
# words="hello world"
# print(words.split(" "))
# print(words.find("ello")) #to find the given str location
# startswith() to find the word starts with the given character if yes true else false
# print(words.startswith("he"))
# # endswith() to find the given string ends with the given charachter
# print(words.endswith("rld"))
# isalpha() is used to find the given string is alphabetic order if yes return true else false
# print(words.isalpha()) #space is not a character
# isdigit() to findn the given string is digit or not
# print(words.isdigit())
# isalnum() used to check the string is number or alphabet
# alnum="123hello"
# print(alnum.isalnum())

word ="Hello world"
print(type(word))


print(word.capitalize())  #first letter becomes capital

print(word.casefold())

print(word.count("l"))


words = word.split("  ")   #return with list
print(words)

print(word.find("wor"))

print(word.startswith("He"))   #return boolean

print(word.endswith("rld"))    #return boolean

print(word.isalpha())          #return boolean


num = "1234"
print(num.isdigit())      #returns with boolean

numal="245wjfjf"
print(numal.isalnum())     #returns with boolean if it contains alphabets and numbers
















