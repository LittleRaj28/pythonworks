text = "hello i am here in kakkanad"
 #print longest word

words=text.split(" ")
print(words)

print(len(words))



print(max(words,key =lambda w:len(w)))


