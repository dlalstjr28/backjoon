listing = []
values= ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
for i in range(3):
    listing.append(input())
result = 1
index = 1
for count,get_color in zip(range(3),listing) :
    exp = values.index(get_color)
    if count == 0 :
        index = index * 10 * exp
    elif count == 1 :
        index += exp
    else :
        result = index*(10 ** exp)
print(result)
