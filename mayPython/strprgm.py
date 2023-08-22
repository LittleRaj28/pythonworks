text = "one  100   and fifty 5"

#100,5




for w in text.split(' '):
    if w.isdigit():
        print(w)

nums = [w for w in text.split(' ') if w.isdigit()]
print(nums)


texts = "England promised to continue its aggressive approach to Test cricket "
vowel =["a","e","i","o","u","E"]
for w in texts.split(" "):
    if w[0].casefold() in vowel:
        print(w)

words = [w for w in texts.split(" ") if w[0].casefold() in vowel]
print(words)