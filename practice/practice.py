def nines(n):
    count = 0
    for i in range(n+1):
        if 9 in i:
            count +=1
    return count
