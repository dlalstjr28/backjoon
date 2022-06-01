number = int(input())
string = ""
for i in range(number) :
    a = str(input())
    if string =="" : 
        string = a
        continue
    else :
        b = ""
        for j in range(len(string)) : 
            if string[j] == a[j] :
                b += a[j]
            else :
                b += "?"
        string = b
print(string)
    
