listing = list(map(int,input().split()))
minute,min_hb,max_hb,up,down = listing[0],listing[1],listing[2],listing[3],listing[4]
check_value_min_hb=min_hb
count_minute = 0
if min_hb + up > max_hb :
    count_minute = -1
    print(count_minute)
else :
    while minute > 0 :
        if min_hb + up > max_hb :
            count_minute +=1
            if min_hb - down < check_value_min_hb : 
                min_hb = check_value_min_hb
            else :
                min_hb -= down
        else :
            minute -= 1
            count_minute +=1
            min_hb += up
    print(count_minute)
