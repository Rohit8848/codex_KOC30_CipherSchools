var1 = input("Enter a phrase=  ")
value = (var1.replace("of","").split())
acronym = ""
for word in value:
  acronym = acronym + word[0].upper()
print(f"Acronym of {var1} is {acronym} ")  