text = input ("enter your tex\n")
if ("make a lot of mony " in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif ("subcribe this" in text):
    spam = True
elif ("watch this" in text):
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")
else:
    print("this text is not spam")
