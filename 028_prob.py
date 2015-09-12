def code(n): 
    total = 1 
    for i in range(1,n+1): 
        for x in range(4): 
            print `(2*i + 1)**2 - 2*x*i`
            total += (2*i + 1)**2 - 2*x*i 
    return total