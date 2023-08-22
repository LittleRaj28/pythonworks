import re
sent = "hi hello hi hi hi hello 13, good afternoon hi hello11:43,78,568 "
ct=sent.count("hi")
print(ct)

nums = re.findall("[0-5][0-9]",sent)
print(nums)
