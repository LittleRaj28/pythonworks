all_users = ["mohanlal","fahad","dq","nivin","asif","vijay"]
dq_friendlists = ["mohanlal","fahad","asif"]
asif_friendlist = ["mohanlal","fahad","nivin","vijay"]

#suggestions for dq

suggestions = set(all_users).difference(set(dq_friendlists))
suggestions.remove("dq")
print(suggestions)

# dq => asif ? mutual friends

mutual = set(dq_friendlists).intersection(set(asif_friendlist))
print(mutual)
