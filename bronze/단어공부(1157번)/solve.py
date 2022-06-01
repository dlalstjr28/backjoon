import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
dictionary = { i : 0 for i in range(len(lowercase))}

case = input()
for i in range(len(case)):
    if case[i] in lowercase :
        dictionary[lowercase.find(case[i])] +=1
    elif case[i] in uppercase :
        dictionary[uppercase.find(case[i])] +=1
    else :
        continue
listing = list(dictionary.values())
maxvalue = listing.count(max(listing))
if maxvalue == 1 :
    print(uppercase[listing.index(max(listing))])
else :
    print("?")
